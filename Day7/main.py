import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Tạo dữ liệu ban đầu và lưu vào CSV
def create_and_save_data():
    data = {
        "Tên": ["An", "Bình", "Chi", "Dũng", "Hà",
                "An", "Bình", "Chi", "Dũng", "Hà",
                "An", "Bình", "Chi", "Dũng", "Hà"],
        "Tuần": [1]*5 + [2]*5 + [3]*5,
        "Bài tập": [5, 4, 6, 3, 4, 6, 5, 7, 4, 5, 7, 6, 8, 5, 6],
        "Điểm": [8.5, 7.0, 9.0, 6.0, 7.5, 9.0, 7.5, 9.5, 7.0, 8.0,
                 9.5, 8.0, 9.8, 7.5, 8.5]
    }
    df = pd.DataFrame(data)
    df.to_csv("progress.csv", index=False)
    print("✅ Đã tạo và lưu dữ liệu vào progress.csv")

# 2. Phân tích dữ liệu tuần
def analyze_weekly_progress(week):
    if not os.path.exists("progress.csv"):
        print("❌ Tệp dữ liệu không tồn tại.")
        return

    df = pd.read_csv("progress.csv")
    week_data = df[df["Tuần"] == week]

    if week_data.empty:
        print(f"❌ Không có dữ liệu cho tuần {week}.")
        return

    avg_exercises = week_data["Bài tập"].mean()
    avg_score = week_data["Điểm"].mean()
    top_student = week_data.loc[week_data["Điểm"].idxmax()]

    print(f"\n📊 Phân tích tuần {week}:")
    print(f"- Bài tập trung bình: {avg_exercises:.2f}")
    print(f"- Điểm trung bình: {avg_score:.2f}")
    print(f"- Học viên xuất sắc: {top_student['Tên']} ({top_student['Điểm']})")

    # Lọc học viên hoàn thành > 4 bài
    filtered = week_data[week_data["Bài tập"] > 4]
    print("\n🎯 Học viên hoàn thành hơn 4 bài:")
    print(filtered[["Tên", "Bài tập", "Điểm"]])

# 3. Trực quan hóa dữ liệu
def visualize_progress():
    if not os.path.exists("progress.csv"):
        print("❌ Tệp dữ liệu không tồn tại.")
        return

    df = pd.read_csv("progress.csv")

    # Biểu đồ đường: điểm trung bình theo tuần
    plt.figure(figsize=(10, 6))
    for name, group in df.groupby("Tên"):
        plt.plot(group["Tuần"], group["Điểm"], marker='o', label=name)
    plt.title("Xu hướng điểm trung bình qua các tuần")
    plt.xlabel("Tuần")
    plt.ylabel("Điểm trung bình")
    plt.legend()
    plt.grid(True)
    plt.savefig("trend.png")
    plt.close()

    # Biểu đồ cột: số bài tập hoàn thành trung bình theo tuần
    bar_data = df.groupby("Tuần")["Bài tập"].mean()
    plt.figure(figsize=(8, 5))
    bar_data.plot(kind="bar", color="skyblue")
    plt.title("Số bài tập hoàn thành trung bình theo tuần")
    plt.xlabel("Tuần")
    plt.ylabel("Bài tập trung bình")
    plt.savefig("comparison.png")
    plt.close()

    print("✅ Đã lưu biểu đồ trend.png và comparison.png")

# 4. Tạo báo cáo tổng kết
def generate_weekly_report():
    if not os.path.exists("progress.csv"):
        print("❌ Tệp dữ liệu không tồn tại.")
        return

    df = pd.read_csv("progress.csv")

    # Tổng bài tập và điểm trung bình theo học viên
    summary = df.groupby("Tên").agg({
        "Bài tập": "sum",
        "Điểm": "mean"
    })

    # Tính học viên tiến bộ nhất
    first_week = df[df["Tuần"] == df["Tuần"].min()]
    last_week = df[df["Tuần"] == df["Tuần"].max()]
    progress = pd.merge(first_week[["Tên", "Điểm"]],
                        last_week[["Tên", "Điểm"]],
                        on="Tên", suffixes=("_đầu", "_cuối"))
    progress["Tăng điểm"] = progress["Điểm_cuối"] - progress["Điểm_đầu"]
    best = progress.loc[progress["Tăng điểm"].idxmax()]

    # Biểu đồ tròn: đóng góp bài tập
    plt.figure(figsize=(7, 7))
    plt.pie(summary["Bài tập"], labels=summary.index, autopct='%1.1f%%')
    plt.title("Tỷ lệ đóng góp bài tập của từng học viên")
    plt.savefig("contribution.png")
    plt.close()

    # Ghi báo cáo ra tệp
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("📄 Báo cáo tổng kết:\n")
        for name, row in summary.iterrows():
            f.write(f"- Tổng bài tập của {name}: {row['Bài tập']}\n")
            f.write(f"- Điểm trung bình của {name}: {row['Điểm']:.2f}\n")
        f.write(f"- Học viên tiến bộ nhất: {best['Tên']} (tăng {best['Tăng điểm']:.2f} điểm)\n")

    print("✅ Đã tạo report.txt và biểu đồ contribution.png")

# 5. Tích hợp chương trình
def main():
    create_and_save_data()
    analyze_weekly_progress(week=2)
    visualize_progress()
    generate_weekly_report()

if __name__ == "__main__":
    main()
