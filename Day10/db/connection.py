from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def setup_database():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["online_store"]

        if "products" not in db.list_collection_names():
            db.create_collection("products")
        if "orders" not in db.list_collection_names():
            db.create_collection("orders")

        print("✅ Đã thiết lập cơ sở dữ liệu và collection.")
        return db
    except ConnectionFailure:
        print("❌ Kết nối MongoDB thất bại.")
        return None
