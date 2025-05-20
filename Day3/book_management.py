# book_management.py

class Book:
    """Lớp cơ bản cho Sách."""
    def __init__(self, book_id, title, author, stock):
        # Sử dụng biến private để bảo vệ mã sách
        self._book_id = book_id
        self.title = title
        self.author = author
        self.stock = stock

    def get_info(self):
        """Trả về thông tin cơ bản của sách."""
        return f"Mã sách: {self._book_id}, Tiêu đề: {self.title}, Tác giả: {self.author}, Tồn kho: {self.stock}"

    def update_stock(self, quantity_change):
        """Cập nhật số lượng tồn kho. Đảm bảo số lượng không âm."""
        new_stock = self.stock + quantity_change
        if new_stock >= 0:
            self.stock = new_stock
            return True
        else:
            print(f"Lỗi: Số lượng tồn kho của sách '{self.title}' không đủ để thực hiện thao tác.")
            return False

    # Phương thức công khai để lấy mã sách nếu cần (không thay đổi trực tiếp)
    def get_book_id(self):
        return self._book_id

class PhysicalBook(Book):
    """Lớp con cho Sách giấy."""
    def __init__(self, book_id, title, author, stock, physical_status):
        super().__init__(book_id, title, author, stock)
        self.physical_status = physical_status

    def get_info(self):
        """Ghi đè phương thức get_info để thêm trạng thái vật lý."""
        base_info = super().get_info()
        return f"{base_info}, Trạng thái vật lý: {self.physical_status}"

class EBook(Book):
    """Lớp con cho Sách điện tử."""
    def __init__(self, book_id, title, author, stock, file_format):
        super().__init__(book_id, title, author, stock)
        self.file_format = file_format
        # Sách điện tử có thể coi là luôn có sẵn, tồn kho chỉ mang tính tượng trưng
        # hoặc biểu thị số lượt có thể mượn đồng thời.
        # Ở đây ta vẫn giữ thuộc tính stock như sách giấy.

    def get_info(self):
        """Ghi đè phương thức get_info để thêm định dạng file."""
        base_info = super().get_info()
        return f"{base_info}, Định dạng file: {self.file_format}"
