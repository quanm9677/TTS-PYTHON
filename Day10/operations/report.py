def generate_report(db):
    print("\n📊 Báo cáo cửa hàng:")
    pipeline = [
        {"$group": {"_id": "$product_id", "doanh_thu": {"$sum": "$total_price"}}}
    ]
    for doc in db.orders.aggregate(pipeline):
        print(f"- Sản phẩm {doc['_id']}: Doanh thu {doc['doanh_thu']} VNĐ")

    low_stock = db.products.count_documents({"stock": {"$lt": 10}})
    print(f"- Sản phẩm tồn kho thấp: {low_stock} sản phẩm")

def cleanup_database(db):
    if "orders" in db.list_collection_names():
        confirm = input("Bạn có muốn xóa collection 'orders'? (y/n): ")
        if confirm.lower() == "y":
            db.orders.drop()
            print("✅ Đã xóa collection 'orders'.")
        else:
            print("⚠️ Không xóa collection.")
