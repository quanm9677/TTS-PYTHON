from pymongo import DESCENDING

def query_orders(db, customer_name):
    print(f"\n🔍 Đơn hàng của {customer_name}:")
    result = db.orders.find(
        {"customer_name": customer_name}
    ).sort("total_price", DESCENDING).limit(5)

    for order in result:
        print(f"- Mã đơn: {order['order_id']}, Sản phẩm: {order['product_id']}, Tổng: {order['total_price']} VNĐ")
