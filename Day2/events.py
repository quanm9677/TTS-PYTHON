# events.py
import numpy as np

def manage_events(events_list, action, **kwargs):
    if action == "add":
        new_event = kwargs.get("event")
        if new_event:
            if any(ev['id'] == new_event['id'] for ev in events_list):
                print(f"Sự kiện với mã {new_event['id']} đã tồn tại.")
            else:
                events_list.append(new_event)
                print(f"Đã thêm sự kiện: {new_event['name']}")
        else:
            print("Không có dữ liệu sự kiện để thêm.")
            
    elif action == "delete":
        event_id = kwargs.get("id")
        if event_id:
            for i, ev in enumerate(events_list):
                if ev['id'] == event_id:
                    del events_list[i]
                    print(f"Đã xóa sự kiện với mã {event_id}")
                    return
            print(f"Không tìm thấy sự kiện với mã {event_id}")
        else:
            print("Không có mã sự kiện để xóa.")
    
    elif action == "update":
        event_id = kwargs.get("id")
        tickets_left = kwargs.get("tickets_left")
        if event_id and tickets_left is not None:
            if tickets_left < 0:
                print("Số lượng vé không thể âm.")
                return
            for ev in events_list:
                if ev['id'] == event_id:
                    ev['tickets_left'] = tickets_left
                    print(f"Cập nhật số vé còn lại cho sự kiện {event_id} thành {tickets_left}")
                    return
            print(f"Không tìm thấy sự kiện với mã {event_id}")
        else:
            print("Thiếu thông tin cập nhật (mã sự kiện hoặc số vé).")
            
    elif action == "access":
        event_id = kwargs.get("id")
        if event_id:
            for ev in events_list:
                if ev['id'] == event_id:
                    print(f"Thông tin sự kiện {event_id}: {ev}")
                    return ev
            print(f"Không tìm thấy sự kiện với mã {event_id}")
        else:
            print("Không có mã sự kiện để truy cập.")
            
    elif action == "list":
        print("Danh sách các sự kiện:")
        for ev in events_list:
            print(ev)
            
    elif action == "average_price":
        prices = np.array([ev['ticket_price'] for ev in events_list])
        avg_price = np.mean(prices)
        print(f"Giá vé trung bình của các sự kiện là: {avg_price:.2f} VNĐ")
        return avg_price
        
    else:
        print("Hành động không hợp lệ.")
