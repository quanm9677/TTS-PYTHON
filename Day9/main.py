from database.setup import setup_database
from models.member import add_members
from models.progress import add_progress, query_progress, update_progress, delete_progress
from reports.summary import generate_summary
from database.cleanup import cleanup_database

def main():
    setup_database()
    add_members()
    add_progress()
    query_progress(1)
    update_progress(1, 45.0, "Hoàn thành sớm")
    # delete_progress(2)
    generate_summary()
    # cleanup_database()  # Bỏ comment nếu muốn xóa bảng weekly_progress

if __name__ == "__main__":
    main()