from database.connection import get_connection
from config.db_config import DB_NAME

def setup_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.database = DB_NAME
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                role VARCHAR(50)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weekly_progress (
                progress_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT,
                week_number INT,
                hours_worked FLOAT CHECK (hours_worked >= 0),
                tasks_completed INT,
                notes TEXT,
                FOREIGN KEY (member_id) REFERENCES members(member_id)
            )
        """)
        print("Đã thiết lập database và các bảng.")
    except Exception as err:
        print("Lỗi khi thiết lập database:", err)
    finally:
        cursor.close()
        conn.close()