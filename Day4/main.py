import json
import re
import pendulum  # Cài đặt: pip install pendulum
from email_validator import validate_email, EmailNotValidError  

# Danh sách khóa học mẫu
COURSES = {
    "KH001": 1000000,
    "KH002": 1500000,
    "KH003": 2000000
}

# Hàm kiểm tra đầu vào
def validate_input(name, email, course_code):
    try:
        # Kiểm tra tên
        if len(name.strip()) < 3:
            raise ValueError("Tên phải có ít nhất 3 ký tự.")

        # Kiểm tra email với thư viện email-validator
        validate_email(email)

        # Kiểm tra mã khóa học
        if not re.match(r"^KH\d{3}$", course_code):
            raise ValueError("Mã khóa học phải có định dạng 'KH' theo sau là 3 chữ số, ví dụ: KH001.")

        # Nếu tất cả hợp lệ
        return True
    except EmailNotValidError as e:
        print(f"Email không hợp lệ: {e}")
    except ValueError as ve:
        print(f"Lỗi: {ve}")
    return False

# Hàm tính chi phí khóa học
def calculate_cost(course_code, quantity, discount_code=None):
    try:
        base_price = COURSES.get(course_code)
        if base_price is None:
            raise ValueError("Mã khóa học không tồn tại.")
        
        total = base_price * quantity

        # Áp dụng mã giảm giá
        if discount_code == "SUMMER25":
            total *= 0.75
        elif discount_code == "EARLYBIRD":
            total *= 0.85

        total = round(total, 2)
        return total
    except Exception as e:
        print(f"Lỗi tính chi phí: {e}")
        return 0

# Hàm lưu dữ liệu vào tệp JSON
def save_registration(name, email, course_code, date_str, cost):
    registration = {
        "name": name,
        "email": email,
        "course_code": course_code,
        "registration_date": date_str,
        "cost": cost
    }
    try:
        try:
            with open("registrations.json", "r", encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(registration)

        with open("registrations.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Lỗi khi lưu đăng ký: {e}")

# Hàm đọc và hiển thị danh sách đăng ký
def load_registrations():
    try:
        with open("registrations.json", "r", encoding='utf-8') as f:
            data = json.load(f)

        print("\n📋 Danh sách đăng ký:")
        for reg in data:
            print(f"Đăng ký của {reg['name']}: Khóa học {reg['course_code']}, Ngày {reg['registration_date']}, Chi phí {reg['cost']} VNĐ")
    except FileNotFoundError:
        print("Chưa có dữ liệu đăng ký.")
    except json.JSONDecodeError:
        print("Lỗi định dạng tệp JSON.")

# Hàm chính tích hợp toàn bộ chương trình
def main():
    print("===== ĐĂNG KÝ KHÓA HỌC TRỰC TUYẾN =====")
    while True:
        try:
            name = input("Nhập họ tên: ").strip()
            email = input("Nhập email: ").strip()
            course_code = input("Nhập mã khóa học (ví dụ: KH001): ").strip().upper()

            if not validate_input(name, email, course_code):
                continue

            quantity = int(input("Nhập số lượng khóa học muốn đăng ký: "))
            if quantity <= 0:
                raise ValueError("Số lượng phải lớn hơn 0.")
                
            discount_code = input("Nhập mã ưu đãi (nếu có): ").strip().upper()

            # Ngày đăng ký hiện tại
            registration_date = pendulum.now().format("YYYY-MM-DD")

            # Tính chi phí
            cost = calculate_cost(course_code, quantity, discount_code)

            # Hiển thị thông báo xác nhận
            print(f"\n✅ Chúc mừng {name} đã đăng ký khóa học {course_code} vào ngày {registration_date}!")
            print(f"💰 Tổng chi phí cho {quantity} khóa học là: {cost} VNĐ.\n")

            # Lưu dữ liệu
            save_registration(name, email, course_code, registration_date, cost)

            # Hiển thị danh sách đăng ký
            load_registrations()

            break
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    main()
