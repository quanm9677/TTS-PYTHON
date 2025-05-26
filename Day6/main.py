import os

def create_weekly_log():
    """
    Tạo một tệp nhật ký tuần mới.
    Yêu cầu người dùng nhập thông tin và ghi vào tệp week_{tuan}.txt.
    """
    try:
        week = int(input("Nhập số tuần (ví dụ: 1): "))
        hours = float(input("Nhập số giờ làm việc trong tuần: "))
        tasks = int(input("Nhập số nhiệm vụ hoàn thành: "))
        notes = input("Nhập ghi chú: ")

        filename = f"week_{week}.txt"

        # Sử dụng 'with' để đảm bảo tệp được đóng sau khi ghi
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Tuần: {week}\n")
            f.write(f"Số giờ làm việc: {hours}\n")
            f.write(f"Nhiệm vụ hoàn thành: {tasks}\n")
            f.write(f"Ghi chú: {notes}\n")

        print(f"Đã tạo nhật ký cho tuần {week} trong tệp {filename}")

    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuần, giờ làm việc và nhiệm vụ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tạo nhật ký: {e}")


def read_weekly_log():
    """
    Đọc nội dung của một tệp nhật ký tuần.
    Yêu cầu người dùng nhập số tuần và in nội dung ra màn hình.
    """
    try:
        week = int(input("Nhập số tuần cần đọc: "))
        filename = f"week_{week}.txt"

        # Kiểm tra sự tồn tại của tệp
        if os.path.exists(filename):
            # Sử dụng 'with' để đảm bảo tệp được đóng sau khi đọc
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                print(f"\n--- Nhật ký tuần {week} ---")
                print(content)
                print("--------------------------\n")
        else:
            print(f"Nhật ký tuần {week} không tồn tại.")

    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuần.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc nhật ký: {e}")


def update_weekly_log():
    """
    Cập nhật nội dung của một tệp nhật ký tuần.
    Yêu cầu người dùng nhập số tuần và thông tin mới, ghi đè lên tệp cũ.
    Nếu tệp không tồn tại, sẽ tạo mới.
    """
    try:
        week = int(input("Nhập số tuần cần cập nhật: "))
        hours = float(input("Nhập số giờ làm việc mới: "))
        tasks = int(input("Nhập số nhiệm vụ hoàn thành mới: "))
        notes = input("Nhập ghi chú mới: ")

        filename = f"week_{week}.txt"

        # Sử dụng chế độ 'w' để ghi đè hoặc tạo mới nếu tệp không tồn tại
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Tuần: {week}\n")
            f.write(f"Số giờ làm việc: {hours}\n")
            f.write(f"Nhiệm vụ hoàn thành: {tasks}\n")
            f.write(f"Ghi chú: {notes}\n")

        print(f"Đã cập nhật nhật ký cho tuần {week} trong tệp {filename}")

    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuần, giờ làm việc và nhiệm vụ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi cập nhật nhật ký: {e}")


def delete_weekly_log():
    """
    Xóa một tệp nhật ký tuần.
    Yêu cầu người dùng nhập số tuần và xóa tệp tương ứng.
    """
    try:
        week = int(input("Nhập số tuần cần xóa: "))
        filename = f"week_{week}.txt"

        # Kiểm tra sự tồn tại của tệp trước khi xóa
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Đã xóa nhật ký tuần {week}.")
        else:
            print(f"Không tìm thấy nhật ký tuần {week} để xóa.")

    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số cho tuần.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xóa nhật ký: {e}")


def generate_summary():
    """
    Tạo báo cáo tổng kết từ tất cả các tệp nhật ký tuần hiện có.
    Tính tổng số giờ và nhiệm vụ, in báo cáo ra màn hình.
    """
    total_hours = 0.0
    total_tasks = 0
    weekly_logs_found = 0

    # Lấy danh sách tất cả các tệp trong thư mục hiện tại
    for filename in os.listdir("."):
        # Kiểm tra nếu tên tệp bắt đầu bằng "week_" và kết thúc bằng ".txt"
        if filename.startswith("week_") and filename.endswith(".txt"):
            try:
                # Đọc từng tệp nhật ký
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    weekly_logs_found += 1
                    # Phân tích nội dung để lấy giờ và nhiệm vụ
                    for line in lines:
                        if line.startswith("Số giờ làm việc:"):
                            try:
                                hours_str = line.split(":")[1].strip()
                                total_hours += float(hours_str)
                            except (IndexError, ValueError):
                                print(f"Cảnh báo: Không thể đọc số giờ từ tệp {filename}. Dòng lỗi: {line.strip()}")
                        elif line.startswith("Nhiệm vụ hoàn thành:"):
                            try:
                                tasks_str = line.split(":")[1].strip()
                                total_tasks += int(tasks_str)
                            except (IndexError, ValueError):
                                print(f"Cảnh báo: Không thể đọc số nhiệm vụ từ tệp {filename}. Dòng lỗi: {line.strip()}")
            except Exception as e:
                print(f"Cảnh báo: Không thể đọc tệp {filename} do lỗi: {e}")

    print("\n--- Báo cáo tổng kết ---")
    print(f"Tổng số tuần: {weekly_logs_found}")
    print(f"Tổng số giờ làm việc: {total_hours}")
    print(f"Tổng nhiệm vụ hoàn thành: {total_tasks}")
    print("-------------------------\n")


def main():
    """
    Hàm chính hiển thị menu và xử lý lựa chọn của người dùng.
    """
    while True:
        print("--- Menu Quản lý Nhật ký Tuần ---")
        print("1. Tạo nhật ký tuần mới")
        print("2. Đọc nhật ký tuần")
        print("3. Cập nhật nhật ký tuần")
        print("4. Xóa nhật ký tuần")
        print("5. Tạo báo cáo tổng kết")
        print("6. Thoát")
        print("---------------------------------")

        choice = input("Nhập lựa chọn của bạn (1-6): ")

        if choice == '1':
            create_weekly_log()
        elif choice == '2':
            read_weekly_log()
        elif choice == '3':
            update_weekly_log()
        elif choice == '4':
            delete_weekly_log()
        elif choice == '5':
            generate_summary()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")

        print("\n") # In dòng trống để dễ nhìn

if __name__ == "__main__":
    main()