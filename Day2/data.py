# data.py
events = [
    {"id": "EV001", "name": "Hội chợ sách", "ticket_price": 50000.0, "tickets_left": 200},
    {"id": "EV002", "name": "Triển lãm tranh", "ticket_price": 75000.0, "tickets_left": 150},
    {"id": "EV003", "name": "Workshop nghệ thuật", "ticket_price": 100000.0, "tickets_left": 100},
    {"id": "EV004", "name": "Lễ hội âm nhạc", "ticket_price": 150000.0, "tickets_left": 300},
    {"id": "EV005", "name": "Hội chợ ẩm thực", "ticket_price": 60000.0, "tickets_left": 250},
]

sponsors = {
    "SP001": ("Công ty A", 5000000.0),
    "SP002": ("Công ty B", 3000000.0),
    "SP003": ("Công ty C", 7000000.0),
}

tickets_sold_today = set()
ticket_transactions = []
