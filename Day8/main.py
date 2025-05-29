import numpy as np
from scipy import stats, optimize
import os

# Tạo và lưu dữ liệu hiệu suất giả định
def create_performance_data(filename='performance.npy'):
    # Tạo dữ liệu ngẫu nhiên cho 5 thành viên, 4 tuần (mỗi tuần là 1 mảng 5x2)
    data = []
    rng = np.random.default_rng(42)
    for _ in range(4):  # 4 tuần
        hours = rng.uniform(30, 45, size=5)  # Giờ làm việc (float)
        tasks = rng.integers(3, 7, size=5)   # Nhiệm vụ hoàn thành (int)
        weekly_data = np.column_stack((hours, tasks))
        data.append(weekly_data)
    np.save(filename, np.array(data))  # Dạng (4 tuần, 5 thành viên, 2 cột)

# Phân tích thống kê cơ bản
def basic_analysis(filename='performance.npy', week_index=0):
    if not os.path.exists(filename):
        print("Tệp dữ liệu không tồn tại.")
        return
    data = np.load(filename)
    if week_index >= data.shape[0]:
        print("Tuần không hợp lệ.")
        return

    week_data = data[week_index]
    hours = week_data[:, 0]
    tasks = week_data[:, 1]

    avg_hours = np.mean(hours)
    std_hours = np.std(hours)
    total_tasks = np.sum(tasks)
    best_member = int(np.argmax(tasks))
    best_tasks = int(tasks[best_member])

    print(f"\nPhân tích tuần {week_index + 1}:")
    print(f"- Trung bình giờ làm: {avg_hours:.2f}")
    print(f"- Độ lệch chuẩn giờ: {std_hours:.2f}")
    print(f"- Tổng nhiệm vụ: {total_tasks}")
    print(f"- Thành viên xuất sắc: Thành viên {best_member + 1} ({best_tasks} nhiệm vụ)")

# Phân tích nâng cao với SciPy
def advanced_analysis(filename='performance.npy'):
    if not os.path.exists(filename):
        print("Tệp dữ liệu không tồn tại.")
        return
    data = np.load(filename)
    combined = np.vstack(data)  # Gộp tất cả các tuần: (20, 2)
    hours = combined[:, 0]
    tasks = combined[:, 1]

    # Hồi quy tuyến tính
    slope, intercept, r_value, p_value, std_err = stats.linregress(hours, tasks)
    correlation, _ = stats.pearsonr(hours, tasks)

    # Tìm outliers: Giờ làm ngoài khoảng [mean ± 2*std]
    mean_hr = np.mean(hours)
    std_hr = np.std(hours)
    lower_bound = mean_hr - 2 * std_hr
    upper_bound = mean_hr + 2 * std_hr
    outliers = hours[(hours < lower_bound) | (hours > upper_bound)]

    print("\nHồi quy tuyến tính:")
    print(f"- Độ dốc: {slope:.4f}")
    print(f"- Hệ số tương quan: {correlation:.4f}")
    print(f"- Giá trị ngoại lai (giờ làm): {outliers if len(outliers) else 'Không có'}")

    return slope, intercept

# Tối ưu hóa phân bổ giờ làm tuần tiếp theo
def optimize_workload(slope, intercept, total_hours=200, members=5):
    # Hàm mục tiêu: tổng nhiệm vụ là âm (vì minimize)
    def objective(x):
        # x: danh sách số giờ làm của từng thành viên
        predicted_tasks = slope * np.array(x) + intercept
        return -np.sum(predicted_tasks)

    # Ràng buộc: tổng số giờ không vượt quá 200
    constraints = {
        'type': 'eq',
        'fun': lambda x: total_hours - np.sum(x)
    }

    # Giới hạn: mỗi thành viên làm từ 30 đến 50 giờ
    bounds = [(30, 50) for _ in range(members)]

    # Khởi tạo với mỗi người 40 giờ
    init = [40] * members

    result = optimize.minimize(objective, init, bounds=bounds, constraints=constraints)

    if result.success:
        print("\nPhân bổ giờ làm tuần tới:")
        for i, h in enumerate(result.x):
            print(f"- Thành viên {i + 1}: {h:.2f} giờ")
        return result.x
    else:
        print("Không thể tối ưu hóa phân bổ giờ làm.")
        return None

# Hàm chính tích hợp toàn bộ quy trình
def main():
    try:
        create_performance_data()
        basic_analysis(week_index=0)
        slope, intercept = advanced_analysis()
        optimize_workload(slope, intercept)
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()

