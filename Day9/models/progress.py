from database.connection import get_connection
from config.db_config import DB_NAME

def add_progress():
    progresses = [
        (1, 1, 40.0, 5, "Hoàn thành đúng hạn"),
        (2, 1, 38.5, 4, "Cần cải thiện tốc độ"),
        (3, 2, 42.0, 6, "Làm việc hiệu quả"),
        (4, 2, 39.0, 5, "Đạt yêu cầu"),
        (5, 3, 45.0, 7, "Quản lý tốt"),
        (1, 2, 41.0, 5, "Ổn định"),
        (2, 2, 37.0, 4, "Cần hỗ trợ"),
        (4, 1, 40.0, 5, "Tốt"),
        (5, 1, 36.0, 3, "Thiếu ý tưởng"),
        (3, 1, 44.0, 6, "Xuất sắc"),
    ]
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO weekly_progress (member_id, week_number, hours_worked, tasks_completed, notes)
            VALUES (%s, %s, %s, %s, %s)
        """, progresses)
        conn.commit()
        print("Đã thêm tiến độ mẫu.")
    except Exception as err:
        print("Lỗi khi thêm tiến độ:", err)
    finally:
        cursor.close()
        conn.close()

def query_progress(week_number):
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        query = """
            SELECT m.name, w.hours_worked, w.tasks_completed, w.notes
            FROM weekly_progress w
            JOIN members m ON w.member_id = m.member_id
            WHERE w.week_number = %s
            ORDER BY w.tasks_completed DESC
            LIMIT 5
        """
        cursor.execute(query, (week_number,))
        results = cursor.fetchall()
        print(f"Tuần {week_number}:")
        for row in results:
            print(f"- {row[0]}: {row[1]} giờ, {row[2]} nhiệm vụ, Ghi chú: {row[3]}")
    except Exception as err:
        print("Lỗi khi truy vấn tiến độ:", err)
    finally:
        cursor.close()
        conn.close()

def update_progress(progress_id, hours_worked, notes):
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE weekly_progress
            SET hours_worked = %s, notes = %s
            WHERE progress_id = %s
        """, (hours_worked, notes, progress_id))
        conn.commit()
        if cursor.rowcount:
            print(f"Đã cập nhật progress_id {progress_id}.")
        else:
            print(f"Không tìm thấy progress_id {progress_id}.")
    except Exception as err:
        print("Lỗi khi cập nhật tiến độ:", err)
    finally:
        cursor.close()
        conn.close()

def delete_progress(week_number):
    try:
        conn = get_connection(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM weekly_progress WHERE week_number = %s", (week_number,))
        conn.commit()
        if cursor.rowcount:
            print(f"Đã xóa {cursor.rowcount} bản ghi tuần {week_number}.")
        else:
            print(f"Không có bản ghi nào để xóa ở tuần {week_number}.")
    except Exception as err:
        print("Lỗi khi xóa tiến độ:", err)
    finally:
        cursor.close()
        conn.close()