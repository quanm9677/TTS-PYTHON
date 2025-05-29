from database.connection import get_connection
from config.db_config import DB_NAME

def generate_summary():
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        query = """
            SELECT m.name, SUM(w.hours_worked), SUM(w.tasks_completed)
            FROM weekly_progress w
            JOIN members m ON w.member_id = m.member_id
            GROUP BY m.name
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("Báo cáo tổng kết:")
        for row in results:
            print(f"- {row[0]}: Tổng {row[1]} giờ, {row[2]} nhiệm vụ")
    except Exception as err:
        print("Lỗi khi tạo báo cáo:", err)
    finally:
        cursor.close()
        conn.close()