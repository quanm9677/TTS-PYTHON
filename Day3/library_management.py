# library_management.py

# Import lớp Book từ module book_management
try:
    from book_management import Book, PhysicalBook, EBook
except ImportError:
    # Xử lý khi chạy file này độc lập hoặc cấu trúc thư mục khác
    print("Không tìm thấy module book_management. Vui lòng đảm bảo file book_management.py tồn tại và cùng cấp.")
    # Định nghĩa lại các lớp rỗng để tránh lỗi khi import fail trong môi trường test
    class Book: pass
    class PhysicalBook(Book): pass
    class EBook(Book): pass


class User:
    """Lớp cho Người dùng."""
    def __init__(self, user_id, name):
        # Sử dụng biến private để bảo vệ mã người dùng
        self._user_id = user_id
        self.name = name
        # Danh sách lưu mã sách đang mượn
        self.borrowed_books = []

    def get_user_id(self):
        """Phương thức công khai để lấy mã người dùng."""
        return self._user_id

    def borrow_book(self, book_id):
        """Thêm mã sách vào danh sách đang mượn."""
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            print(f"Người dùng '{self.name}' đã mượn sách có mã '{book_id}'.")
            return True
        else:
            print(f"Người dùng '{self.name}' đã mượn sách có mã '{book_id}' rồi.")
            return False

    def return_book(self, book_id):
        """Xóa mã sách khỏi danh sách đang mượn."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            print(f"Người dùng '{self.name}' đã trả sách có mã '{book_id}'.")
            return True
        else:
            print(f"Người dùng '{self.name}' không mượn sách có mã '{book_id}'.")
            return False

    def get_borrowed_books(self):
        """Trả về danh sách mã sách đang mượn."""
        return self.borrowed_books

class Library:
    """Lớp quản lý danh sách sách trong thư viện."""
    def __init__(self):
        self.books = [] # Danh sách chứa các đối tượng Book (PhysicalBook hoặc EBook)
        self._iterator_index = 0 # Index cho iterator

    def add_book(self, book):
        """Thêm một đối tượng sách vào thư viện."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Đã thêm sách '{book.title}' vào thư viện.")
        else:
            print("Đối tượng thêm vào không phải là sách hợp lệ.")

    def find_book_by_id(self, book_id):
        """Tìm sách theo mã sách."""
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None # Trả về None nếu không tìm thấy sách

    # Triển khai Iterator
    def __iter__(self):
        """Khởi tạo iterator."""
        # Sắp xếp sách theo tiêu đề trước khi duyệt
        self.books.sort(key=lambda book: book.title)
        self._iterator_index = 0
        return self

    def __next__(self):
        """Trả về cuốn sách tiếp theo."""
        if self._iterator_index < len(self.books):
            book = self.books[self._iterator_index]
            self._iterator_index += 1
            return book
        else:
            # Dừng iterator khi hết sách
            raise StopIteration

def display_books(book_list):
    """Hàm hiển thị thông tin sách, thể hiện tính đa hình."""
    print("\n--- Danh sách sách (sử dụng Polymorphism) ---")
    if not book_list:
        print("Thư viện không có sách nào.")
        return

    for book in book_list:
        # Gọi phương thức get_info, sẽ tự động gọi phương thức phù hợp
        # của lớp con (PhysicalBook hoặc EBook)
        print(book.get_info())
    print("-------------------------------------------")
