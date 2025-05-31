def update_order(db, order_id, new_quantity):
    orders = db.orders
    order = orders.find_one({"order_id": order_id})
    if not order:
        print("❌ Không tìm thấy đơn hàng.")
        return

    product = db.products.find_one({"product_id": order["product_id"]})
    if not product:
        print("❌ Không tìm thấy sản phẩm.")
        return

    new_total = product["price"] * new_quantity
    orders.update_one(
        {"order_id": order_id},
        {"$set": {"quantity": new_quantity, "total_price": new_total}}
    )
    print(f"✅ Đã cập nhật đơn hàng {order_id} (số lượng: {new_quantity}, tổng: {new_total} VNĐ).")
