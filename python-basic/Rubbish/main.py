import data_manager
# Import module của các bạn khác (Bỏ comment khi file họ đã sẵn sàng)
# import mod_client
# import mod_delivery
# import mod_product

def dang_nhap():
    print("\n--- SEND2YOU LOGIN ---")
    user_in = input("Tài khoản (SĐT/Login): ")
    pass_in = input("Mật khẩu: ")
    
    # 1. Gọi Adapter để lấy dữ liệu tổng hợp
    df_users = data_manager.load_all_users_for_login()
    
    if df_users.empty:
        print("❌ Lỗi: Không đọc được dữ liệu người dùng!")
        return None

    # 2. Tìm kiếm (User & Pass)
    # Lưu ý: id và pass đã được chuyển thành chuỗi (str) nên so sánh rất an toàn
    ket_qua = df_users.loc[(df_users["id"] == user_in) & (df_users["pass"] == pass_in)]
    
    if not ket_qua.empty:
        found_user = ket_qua.iloc[0]
        print(f"✅ Xin chào: {found_user['name']} (Vai trò: {found_user['role']})")
        return found_user # Trả về thẻ bài (gồm id, role, name)
    else:
        print("❌ Sai tài khoản hoặc mật khẩu!")
        return None

def main():
    while True:
        print("\n=== MENU CHÍNH ===")
        print("1. Đăng nhập")
        print("2. Đăng ký (Khách mới)")
        print("0. Thoát")
        
        chon = input(">> Chọn: ")
        
        if chon == "1":
            user = dang_nhap()
            if user is not None:
                role = user['role']
                user_id = user['id']
                
                # --- ĐIỀU HƯỚNG ---
                if role == 'client':
                    print("--> Đang mở Module Khách Hàng...")
                    # mod_client.menu_khach(user_id)
                    
                elif role == 'estafeta':
                    print("--> Đang mở Module Shipper...")
                    # mod_delivery.menu_shipper(user_id)
                    
                elif role == 'manager':
                    print("--> Đang mở Module Quản Lý...")
                    # mod_product.menu_quan_ly()
                    
        elif chon == "2":
            print(">> Chức năng đăng ký đang bảo trì...")
            
        elif chon == "0":
            print("Tạm biệt!")
            break

if __name__ == "__main__":
    main()