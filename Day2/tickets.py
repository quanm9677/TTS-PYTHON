# tickets.py

def process_tickets(action, tickets_sold_today, ticket_transactions, **kwargs):
    if action == "add":
        transaction = kwargs.get("transaction")
        if transaction:
            event_id = transaction.get("event_id")
            quantity = transaction.get("quantity")
            if not event_id or quantity is None:
                print("Thiếu thông tin giao dịch.")
                return
            if quantity < 0:
                print("Số lượng vé không thể âm.")
                return
            ticket_transactions.append(transaction)
            if quantity > 0:
                tickets_sold_today.add(event_id)
            print(f"Thêm giao dịch bán vé: {transaction}")
        else:
            print("Không có dữ liệu giao dịch để thêm.")
    
    elif action == "check":
        event_id = kwargs.get("event_id")
        if event_id:
            if event_id in tickets_sold_today:
                print(f"Sự kiện {event_id} có vé đã bán trong ngày.")
                return True
            else:
                print(f"Sự kiện {event_id} chưa có vé bán trong ngày.")
                return False
        else:
            print("Không có mã sự kiện để kiểm tra.")
    
    elif action == "list":
        print("Danh sách giao dịch bán vé theo sự kiện:")
        grouped = {}
        for trans in ticket_transactions:
            eid = trans['event_id']
            grouped.setdefault(eid, []).append(trans)
        for eid, trans_list in grouped.items():
            print(f"Sự kiện {eid}:")
            for t in trans_list:
                print(f"  Mã vé: {t['ticket_id']}, Số lượng: {t['quantity']}")
    
    elif action == "delete_zero":
        before = len(ticket_transactions)
        ticket_transactions[:] = [t for t in ticket_transactions if t['quantity'] != 0]
        after = len(ticket_transactions)
        print(f"Đã xóa {before - after} giao dịch có số lượng vé bằng 0.")
    
    else:
        print("Hành động không hợp lệ.")
