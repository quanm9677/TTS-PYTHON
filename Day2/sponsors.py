# sponsors.py
def manage_sponsors(sponsors_dict, action, **kwargs):
    if action == "add":
        sp_id = kwargs.get("id")
        name = kwargs.get("name")
        amount = kwargs.get("amount")
        if sp_id and name and amount is not None:
            if sp_id in sponsors_dict:
                print(f"Nhà tài trợ với mã {sp_id} đã tồn tại.")
            else:
                sponsors_dict[sp_id] = (name, amount)
                print(f"Đã thêm nhà tài trợ: {name} với số tiền {amount}")
        else:
            print("Thiếu thông tin nhà tài trợ để thêm.")
            
    elif action == "delete":
        sp_id = kwargs.get("id")
        if sp_id:
            if sp_id in sponsors_dict:
                del sponsors_dict[sp_id]
                print(f"Đã xóa nhà tài trợ với mã {sp_id}")
            else:
                print(f"Không tìm thấy nhà tài trợ với mã {sp_id}")
        else:
            print("Không có mã nhà tài trợ để xóa.")
    
    elif action == "update":
        sp_id = kwargs.get("id")
        amount = kwargs.get("amount")
        if sp_id and amount is not None:
            if sp_id in sponsors_dict:
                name = sponsors_dict[sp_id][0]
                sponsors_dict[sp_id] = (name, amount)
                print(f"Cập nhật số tiền tài trợ của nhà tài trợ {sp_id} thành {amount}")
            else:
                print(f"Không tìm thấy nhà tài trợ với mã {sp_id}")
        else:
            print("Thiếu thông tin cập nhật (mã hoặc số tiền).")
            
    elif action == "access":
        sp_id = kwargs.get("id")
        if sp_id:
            if sp_id in sponsors_dict:
                print(f"Thông tin nhà tài trợ {sp_id}: {sponsors_dict[sp_id]}")
                return sponsors_dict[sp_id]
            else:
                print(f"Không tìm thấy nhà tài trợ với mã {sp_id}")
        else:
            print("Không có mã nhà tài trợ để truy cập.")
            
    elif action == "list":
        print("Danh sách nhà tài trợ:")
        for sp_id, info in sponsors_dict.items():
            print(f"{sp_id}: Tên: {info[0]}, Số tiền: {info[1]}")
            
    else:
        print("Hành động không hợp lệ.")
