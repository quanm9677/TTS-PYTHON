from db.connection import setup_database
from data.add_data import add_data
from operations.query import query_orders
from operations.update import update_order
from operations.delete import delete_order
from operations.report import generate_report, cleanup_database

def main():
    db = setup_database()
    if db is not None:
        add_data(db)
        query_orders(db, "Nguyễn Văn A")
        update_order(db, "DH001", 3)
        delete_order(db)
        generate_report(db)
        cleanup_database(db)

if __name__ == "__main__":
    main()
