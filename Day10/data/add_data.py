def add_data(db):
    products = db["products"]
    orders = db["orders"]

    product_data = [
        {"product_id": "SP001", "name": "Áo thun", "price": 150000.0, "stock": 50},
        {"product_id": "SP002", "name": "Quần jean", "price": 350000.0, "stock": 20},
        {"product_id": "SP003", "name": "Giày sneaker", "price": 800000.0, "stock": 15},
        {"product_id": "SP004", "name": "Mũ lưỡi trai", "price": 100000.0, "stock": 35},
        {"product_id": "SP005", "name": "Balo", "price": 250000.0, "stock": 10}
    ]
    products.insert_many(product_data)

    order_data = [
        {"order_id": "DH001", "customer_name": "Nguyễn Văn A", "product_id": "SP001", "quantity": 2, "total_price": 300000.0, "order_date": "2025-04-01"},
        {"order_id": "DH002", "customer_name": "Trần Thị B", "product_id": "SP002", "quantity": 1, "total_price": 350000.0, "order_date": "2025-04-02"},
        {"order_id": "DH003", "customer_name": "Lê Văn C", "product_id": "SP003", "quantity": 1, "total_price": 800000.0, "order_date": "2025-04-03"},
        {"order_id": "DH004", "customer_name": "Nguyễn Văn A", "product_id": "SP005", "quantity": 2, "total_price": 500000.0, "order_date": "2025-04-04"},
        {"order_id": "DH005", "customer_name": "Trần Thị B", "product_id": "SP004", "quantity": 3, "total_price": 300000.0, "order_date": "2025-04-05"},
        {"order_id": "DH006", "customer_name": "Lê Văn C", "product_id": "SP003", "quantity": 2, "total_price": 1600000.0, "order_date": "2025-04-06"},
        {"order_id": "DH007", "customer_name": "Nguyễn Văn A", "product_id": "SP002", "quantity": 1, "total_price": 350000.0, "order_date": "2025-04-07"},
        {"order_id": "DH008", "customer_name": "Trần Thị B", "product_id": "SP001", "quantity": 4, "total_price": 600000.0, "order_date": "2025-04-08"},
        {"order_id": "DH009", "customer_name": "Nguyễn Văn A", "product_id": "SP004", "quantity": 1, "total_price": 100000.0, "order_date": "2025-04-09"},
        {"order_id": "DH010", "customer_name": "Lê Văn C", "product_id": "SP005", "quantity": 1, "total_price": 250000.0, "order_date": "2025-04-10"}
    ]
    orders.insert_many(order_data)

    print("✅ Đã thêm dữ liệu mẫu.")
