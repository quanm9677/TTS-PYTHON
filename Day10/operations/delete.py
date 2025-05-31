def delete_order(db):
    result = db.orders.delete_many({"total_price": {"$lt": 100000}})
    print(f"🗑️ Đã xóa {result.deleted_count} đơn hàng có tổng giá trị dưới 100000 VNĐ.")
