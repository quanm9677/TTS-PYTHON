# main.py
from data import events, sponsors, tickets_sold_today, ticket_transactions
from events import manage_events
from sponsors import manage_sponsors
from tickets import process_tickets
from report import generate_report

def main():
    print("Khởi tạo dữ liệu mẫu...\n")
    
    print("=== Quản lý sự kiện ===")
    # Thêm một sự kiện mới
    new_event = {"id": "EV006", "name": "Triển lãm nhiếp ảnh", "ticket_price": 80000.0, "tickets_left": 120}
    manage_events(events, "add", event=new_event)
    
    # Cập nhật số vé còn lại cho sự kiện EV003
    manage_events(events, "update", id="EV003", tickets_left=90)
    
    # Duyệt và in danh sách sự kiện
    manage_events(events, "list")
    
    # Tính giá vé trung bình
    manage_events(events, "average_price")
    
    print("\n=== Quản lý nhà tài trợ ===")
    # Thêm nhà tài trợ mới
    manage_sponsors(sponsors, "add", id="SP004", name="Công ty D", amount=4500000.0)
    
    # Truy cập thông tin nhà tài trợ SP002
    manage_sponsors(sponsors, "access", id="SP002")
    
    # Cập nhật số tiền tài trợ cho SP001
    manage_sponsors(sponsors, "update", id="SP001", amount=6000000.0)
    
    # Duyệt và in danh sách nhà tài trợ
    manage_sponsors(sponsors, "list")
    
    print("\n=== Quản lý vé đã bán ===")
    # Thêm giao dịch bán vé
    trans1 = {"event_id": "EV001", "ticket_id": "TICKET_001", "quantity": 5}
    trans2 = {"event_id": "EV003", "ticket_id": "TICKET_002", "quantity": 10}
    
    process_tickets("add", tickets_sold_today, ticket_transactions, transaction=trans1)
    process_tickets("add", tickets_sold_today, ticket_transactions, transaction=trans2)
    
    # Kiểm tra vé bán cho EV001
    process_tickets("check", tickets_sold_today, ticket_transactions, event_id="EV001")
    
    # In danh sách giao dịch bán vé
    process_tickets("list", tickets_sold_today, ticket_transactions)
    
    # Xóa giao dịch có số lượng vé bằng 0 (nếu có)
    process_tickets("delete_zero", tickets_sold_today, ticket_transactions)
    
    print("\n=== Báo cáo thống kê ===")
    generate_report(events, ticket_transactions)


if __name__ == "__main__":
    main()
