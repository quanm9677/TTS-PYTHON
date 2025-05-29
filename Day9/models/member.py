from database.connection import get_connection
from config.db_config import DB_NAME

def add_members():
    members = [
        ("An", "Developer"),
        ("Bình", "Tester"),
        ("Cường", "Manager"),
        ("Dương", "Developer"),
        ("Hà", "Designer"),
    ]
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO members (name, role) VALUES (%s, %s)", members)
        conn.commit()
        print("Đã thêm thành viên mẫu.")
    except Exception as err:
        print("Lỗi khi thêm thành viên:", err)
    finally:
        cursor.close()
        conn.close()