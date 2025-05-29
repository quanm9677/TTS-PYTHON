from database.connection import get_connection
from config.db_config import DB_NAME

def cleanup_database():
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = %s AND table_name = 'weekly_progress'
        """, (DB_NAME,))
        if cursor.fetchone()[0]:
            cursor.execute("DROP TABLE weekly_progress")
            print("Đã xóa bảng weekly_progress.")
        else:
            print("Bảng weekly_progress không tồn tại.")
        conn.commit()
    except Exception as err:
        print("Lỗi khi dọn dẹp database:", err)
    finally:
        cursor.close()
        conn.close()