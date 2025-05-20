# main.py

# Import các lớp và hàm từ các module đã tạo
try:
    from book_management import PhysicalBook, EBook
    from library_management import User, Library, display_books
except ImportError:
    print("Lỗi: Không tìm thấy các module book_management hoặc library_management.")
    print("Vui lòng đảm bảo các file Python tương ứng nằm cùng cấp.")
    exit() # Thoát chương trình nếu import thất bại

def main():
    """Hàm chính để chạy chương trình quản lý thư viện."""

    # 1. Tạo đối tượng Library
    library = Library()

    # 2. Tạo và thêm sách vào thư viện
    print("--- Thêm sách vào thư viện ---")
    book1 = PhysicalBook("B001", "Cuốn Theo Chiều Gió", "Margaret Mitchell", 5, "Mới")
    book2 = PhysicalBook("B002", "Nhà Giả Kim", "Paulo Coelho", 3, "Cũ vừa")
    book3 = PhysicalBook("B003", "Đắc Nhân Tâm", "Dale Carnegie", 7, "Mới")
    book4 = EBook("E001", "1984", "George Orwell", 100, "PDF") # Tồn kho sách điện tử có thể lớn
    book5 = EBook("E002", "Anh Em Nhà Karamazov", "Fyodor Dostoevsky", 50, "EPUB")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    print("------------------------------")

    # 3. Tạo đối tượng User
    print("\n--- Tạo người dùng ---")
    user1 = User("U001", "Nguyen Van A")
    user2 = User("U002", "Tran Thi B")
    print(f"Đã tạo người dùng: {user1.name} ({user1.get_user_id()}), {user2.name} ({user2.get_user_id()})")
    print("----------------------")

    # 4. Thực hiện mượn sách
    print("\n--- Thực hiện mượn sách ---")
    # User 1 mượn 2 sách
    print(f"Người dùng '{user1.name}' thực hiện mượn:")
    book_to_borrow1_id = "B001" # Cuốn Theo Chiều Gió
    book_to_borrow2_id = "E001" # 1984

    # Kiểm tra và cập nhật tồn kho khi mượn sách giấy
    book_to_borrow1 = library.find_book_by_id(book_to_borrow1_id)
    if book_to_borrow1 and isinstance(book_to_borrow1, PhysicalBook):
         if book_to_borrow1.update_stock(-1): # Giảm tồn kho
             user1.borrow_book(book_to_borrow1_id)
         else:
             print(f"Không thể mượn sách '{book_to_borrow1.title}' do hết hàng.")
    elif book_to_borrow1 and isinstance(book_to_borrow1, EBook):
         # Đối với Ebook, chỉ cần thêm vào danh sách mượn của người dùng
         # Tồn kho có thể không cần giảm hoặc giảm theo logic khác tùy quy định
         user1.borrow_book(book_to_borrow1_id)
    else:
        print(f"Không tìm thấy sách có mã '{book_to_borrow1_id}'.")


    book_to_borrow2 = library.find_book_by_id(book_to_borrow2_id)
    if book_to_borrow2 and isinstance(book_to_borrow2, PhysicalBook):
         if book_to_borrow2.update_stock(-1): # Giảm tồn kho
             user1.borrow_book(book_to_borrow2_id)
         else:
             print(f"Không thể mượn sách '{book_to_borrow2.title}' do hết hàng.")
    elif book_to_borrow2 and isinstance(book_to_borrow2, EBook):
         user1.borrow_book(book_to_borrow2_id)
    else:
        print(f"Không tìm thấy sách có mã '{book_to_borrow2_id}'.")


    # User 2 mượn 2 sách
    print(f"\nNgười dùng '{user2.name}' thực hiện mượn:")
    book_to_borrow3_id = "B002" # Nhà Giả Kim
    book_to_borrow4_id = "B003" # Đắc Nhân Tâm
    book_to_borrow5_id = "B999" # Sách không tồn tại

    book_to_borrow3 = library.find_book_by_id(book_to_borrow3_id)
    if book_to_borrow3 and isinstance(book_to_borrow3, PhysicalBook):
         if book_to_borrow3.update_stock(-1):
             user2.borrow_book(book_to_borrow3_id)
         else:
             print(f"Không thể mượn sách '{book_to_borrow3.title}' do hết hàng.")
    elif book_to_borrow3 and isinstance(book_to_borrow3, EBook):
         user2.borrow_book(book_to_borrow3_id)
    else:
        print(f"Không tìm thấy sách có mã '{book_to_borrow3_id}'.")

    book_to_borrow4 = library.find_book_by_id(book_to_borrow4_id)
    if book_to_borrow4 and isinstance(book_to_borrow4, PhysicalBook):
         if book_to_borrow4.update_stock(-1):
             user2.borrow_book(book_to_borrow4_id)
         else:
             print(f"Không thể mượn sách '{book_to_borrow4.title}' do hết hàng.")
    elif book_to_borrow4 and isinstance(book_to_borrow4, EBook):
         user2.borrow_book(book_to_borrow4_id)
    else:
        print(f"Không tìm thấy sách có mã '{book_to_borrow4_id}'.")

    book_to_borrow5 = library.find_book_by_id(book_to_borrow5_id)
    if book_to_borrow5 and isinstance(book_to_borrow5, PhysicalBook):
         if book_to_borrow5.update_stock(-1):
             user2.borrow_book(book_to_borrow5_id)
         else:
             print(f"Không thể mượn sách '{book_to_borrow5.title}' do hết hàng.")
    elif book_to_borrow5 and isinstance(book_to_borrow5, EBook):
         user2.borrow_book(book_to_borrow5_id)
    else:
        print(f"Không tìm thấy sách có mã '{book_to_borrow5_id}'.") # Kiểm tra sách không tồn tại
    print("------------------------------")

    # 5. Thực hiện trả sách
    print("\n--- Thực hiện trả sách ---")
    # User 1 trả 1 sách
    book_to_return_id = "B001" # Cuốn Theo Chiều Gió
    print(f"Người dùng '{user1.name}' thực hiện trả:")
    book_to_return = library.find_book_by_id(book_to_return_id)
    if book_to_return:
        if user1.return_book(book_to_return_id):
            # Chỉ cập nhật tồn kho nếu sách được trả thành công
            if isinstance(book_to_return, PhysicalBook):
                 book_to_return.update_stock(1) # Tăng tồn kho
        else:
             print(f"Không thể trả sách có mã '{book_to_return_id}' vì người dùng không mượn.")
    else:
        print(f"Không tìm thấy sách có mã '{book_to_return_id}'.")

    # User 2 cố gắng trả sách không mượn
    book_to_return_id_fail = "E001"
    print(f"\nNgười dùng '{user2.name}' thực hiện trả (sách không mượn):")
    book_to_return_fail = library.find_book_by_id(book_to_return_id_fail)
    if book_to_return_fail:
         if user2.return_book(book_to_return_id_fail):
            if isinstance(book_to_return_fail, PhysicalBook):
                 book_to_return_fail.update_stock(1)
         else:
             print(f"Không thể trả sách có mã '{book_to_return_id_fail}' vì người dùng không mượn.")
    else:
         print(f"Không tìm thấy sách có mã '{book_to_return_id_fail}'.")
    print("--------------------------")

    # 6. Sử dụng Iterator để duyệt và in thông tin tất cả sách trong thư viện
    print("\n--- Duyệt sách bằng Iterator ---")
    if not library.books:
        print("Thư viện không có sách nào để duyệt.")
    else:
        # Duyệt qua đối tượng library, tự động gọi __iter__ và __next__
        for book in library:
            print(book.get_info())
    print("-------------------------------")

    # 7. Gọi hàm display_books để hiển thị thông tin sách, thể hiện tính đa hình
    display_books(library.books)

    # 8. In danh sách sách đang mượn của từng người dùng
    print("\n--- Danh sách sách đang mượn ---")
    print(f"Người dùng '{user1.name}': {user1.get_borrowed_books()}")
    print(f"Người dùng '{user2.name}': {user2.get_borrowed_books()}")
    print("--------------------------------")

# Khối này đảm bảo hàm main() chỉ chạy khi file main.py được thực thi trực tiếp
if __name__ == "__main__":
    main()
