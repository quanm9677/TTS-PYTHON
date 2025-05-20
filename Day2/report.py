# report.py
import numpy as np

def generate_report(events_list, ticket_transactions):
    nearly_sold_out = [ev['name'] for ev in events_list if ev['tickets_left'] < 20]
    
    prices = np.array([ev['ticket_price'] for ev in events_list])
    tickets_left = np.array([ev['tickets_left'] for ev in events_list])
    total_value = np.sum(prices * tickets_left)
    
    sold_event_ids = set(t['event_id'] for t in ticket_transactions)
    
    print("\n--- Báo cáo thống kê ---")
    if nearly_sold_out:
        print("Sự kiện sắp hết vé:")
        for name in nearly_sold_out:
            print(f" - {name}")
    else:
        print("Không có sự kiện nào sắp hết vé.")
    
    print(f"Tổng giá trị vé còn lại: {total_value:.2f} VNĐ")
    
    if sold_event_ids:
        print("Sự kiện đã bán vé:")
        for eid in sold_event_ids:
            print(f" - {eid}")
    else:
        print("Chưa có sự kiện nào bán vé.")
    print("------------------------\n")
