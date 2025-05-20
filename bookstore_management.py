# -------------------------------
# Khởi tạo dữ liệu: danh sách sách và thông tin khách hàng
# -------------------------------

# Danh sách sách: mỗi cuốn là một dictionary
books = [
    {"ten": "Dế Mèn Phiêu Lưu Ký", "gia": 45000, "ton_kho": 20, "da_ban": 15},
    {"ten": "Tuổi Thơ Dữ Dội", "gia": 65000, "ton_kho": 5, "da_ban": 8},
    {"ten": "Harry Potter", "gia": 120000, "ton_kho": 10, "da_ban": 25},
    {"ten": "Đắc Nhân Tâm", "gia": 85000, "ton_kho": 0, "da_ban": 30},
    {"ten": "Sherlock Holmes", "gia": 99000, "ton_kho": 7, "da_ban": 12}
]

# Thông tin khách hàng
ten_khach = "An"
loai_khach = "VIP"  # hoặc "thường"

# -------------------------------
# Hàm tính tiền hóa đơn
# -------------------------------

def calculate_bill(ten_sach, so_luong_mua, loai_khach):
    # Kiểm tra số lượng hợp lệ
    if not isinstance(so_luong_mua, int) or so_luong_mua <= 0:
        return "Số lượng mua phải là số nguyên dương.", 0.0

    for book in books:
        if book["ten"].lower() == ten_sach.lower():
            if book["ton_kho"] <= 0:
                return f"Sách '{ten_sach}' đã hết hàng.", 0.0
            elif book["ton_kho"] < so_luong_mua:
                return f"Không đủ số lượng tồn kho cho '{ten_sach}'.", 0.0
            else:
                tong_tien = book["gia"] * so_luong_mua
                if loai_khach.lower() == "vip":
                    tong_tien *= 0.9  # Giảm 10%
                # Cập nhật tồn kho và số lượng bán
                book["ton_kho"] -= so_luong_mua
                book["da_ban"] += so_luong_mua
                return f"Tổng tiền cho sách '{ten_sach}' là: {tong_tien:.2f} VNĐ", tong_tien

    return "Sách không tồn tại trong hệ thống.", 0.0

# -------------------------------
# Hàm kiểm tra tồn kho và phân loại giá
# -------------------------------

def check_stock(ten_sach, so_luong_mua):
    for book in books:
        if book["ten"].lower() == ten_sach.lower():
            # Kiểm tra tồn kho
            if book["ton_kho"] >= so_luong_mua:
                print("Còn hàng")
                stock_status = True
            else:
                print("Hết hàng hoặc không đủ")
                stock_status = False

            # Phân loại sách theo giá
            match book["gia"]:
                case gia if gia < 50000:
                    loai_gia = "Sách giá rẻ"
                case gia if 50000 <= gia <= 100000:
                    loai_gia = "Sách trung bình"
                case _:
                    loai_gia = "Sách cao cấp"

            return stock_status, loai_gia

    return False, "Không tìm thấy sách"

# -------------------------------
# Tạo mã giảm giá bằng Lambda
# -------------------------------

# Tạo lambda function cho mã giảm giá
tao_ma_giam_gia = lambda ten, loai: ten.upper() + "_VIP" if loai.lower() == "vip" else ten.upper() + "_REG"

# -------------------------------
# In sách bán chạy (For loop & While loop)
# -------------------------------

def thong_ke_ban_chay():
    print("\n📚 Các sách bán chạy (bán > 10 cuốn):")
    for book in books:
        if book["da_ban"] > 10:
            print(f"- {book['ten']} ({book['da_ban']} cuốn)")

    # Tìm sách bán chạy nhất (While loop)
    max_ban = -1
    best_seller = None
    i = 0
    while i < len(books):
        if books[i]["da_ban"] > max_ban:
            max_ban = books[i]["da_ban"]
            best_seller = books[i]
        i += 1

    if best_seller:
        print("\n🏆 Sách bán chạy nhất:")
        print(f"Tên: {best_seller['ten']}, Đã bán: {best_seller['da_ban']} cuốn")

# -------------------------------
# Hàm main để tích hợp chương trình
# -------------------------------

def main():
    print("=== Quản lý cửa hàng sách nhỏ ===\n")

    # Ví dụ: Gọi hàm tính hóa đơn
    ket_qua, tien = calculate_bill("Harry Potter", 2, loai_khach)
    print(ket_qua)

    # Gọi hàm kiểm tra tồn kho + phân loại
    trang_thai, loai_sach = check_stock("Harry Potter", 2)
    print(f"Phân loại giá: {loai_sach}")

    # In mã giảm giá
    ma = tao_ma_giam_gia(ten_khach, loai_khach)
    print(f"\n🎁 Mã giảm giá cho khách hàng: {ma}")

    # In danh sách sách bán chạy
    thong_ke_ban_chay()

# -------------------------------
# Chạy chương trình
# -------------------------------

if __name__ == "__main__":
    main()
