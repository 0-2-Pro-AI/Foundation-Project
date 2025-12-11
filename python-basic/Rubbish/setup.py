import pandas as pd
import os

# Tên file CHÍNH XÁC theo ảnh bạn gửi
FILE_CLIENTS = "login_client.csv"
FILE_STAFF = "works_delivery.csv"
FILE_PRODUCTS = "products_stock.csv" # Họ đặt tên này
FILE_ORDERS = "orders.csv"           # File mình tạo riêng chuẩn hóa
FILE_COMPLAINTS = "complaints.csv"

def create_data_final():
    print("🛡️ Đang kiểm tra dữ liệu hệ thống...")

    # 1. CLIENTS (Khớp ảnh login_client.csv)
    if not os.path.exists(FILE_CLIENTS):
        data_clients = {
            "Name": ["Joao Pereira", "Maria Fernandes"],
            "Contact": ["961219231", "930153233"], # ID đăng nhập
            "Password": ["client1", "client2"],
            "Address": ["Travessia Amelia Rodrigues", "Rua Antonio Fonseca"],
            "ZP1": ["152", "743"],
            "ZP2": ["4700", "4720"],
            "Orders": ["103", "336"]
        }
        # Lưu ý: sep=';' là quan trọng nhất
        pd.DataFrame(data_clients).to_csv(FILE_CLIENTS, index=False, sep=';')
        print(f"✅ Đã tạo mới: {FILE_CLIENTS}")
    else:
        print(f"⏩ Đã có file {FILE_CLIENTS} (Giữ nguyên)")

    # 2. STAFF (Khớp ảnh works_delivery.csv)
    if not os.path.exists(FILE_STAFF):
        data_staff = {
            "Login": ["109609", "113168"],
            "Password": ["Yeidman", "Andre"],
            "Zone": ["Gestor", "Center"], # Gestor -> Admin, Center -> Shipper
            "Work_Hour": ["all_day", "week_morning"]
        }
        pd.DataFrame(data_staff).to_csv(FILE_STAFF, index=False, sep=';')
        print(f"✅ Đã tạo mới: {FILE_STAFF}")
    else:
        print(f"⏩ Đã có file {FILE_STAFF} (Giữ nguyên)")

    # 3. PRODUCTS (Khớp ảnh products_stock.csv)
    if not os.path.exists(FILE_PRODUCTS):
        data_products = {
            "Id": [2001, 2002, 2003, 2004, 2005],
            "Product": ["Flores variadas", "Rosas", "Lirios", "Tuplipas", "Margaridas"],
            "Quantity in stock": [250, 500, 150, 175, 200],
            "Unite price": ["3,00", "5,00", "12,00", "15,00", "8,00"] # Giá kiểu Bồ Đào Nha
        }
        pd.DataFrame(data_products).to_csv(FILE_PRODUCTS, index=False, sep=';')
        print(f"✅ Đã tạo mới: {FILE_PRODUCTS}")
    else:
        print(f"⏩ Đã có file {FILE_PRODUCTS} (Giữ nguyên)")

    # 4. ORDERS (File chuẩn của bạn)
    if not os.path.exists(FILE_ORDERS):
        cols = ["order_id", "client_id", "product_id", "status", "shipper_id"]
        pd.DataFrame(columns=cols).to_csv(FILE_ORDERS, index=False, sep=';')
        print(f"✅ Đã tạo mới: {FILE_ORDERS}")
    else:
        print(f"⏩ Đã có file {FILE_ORDERS}")

    # 5. COMPLAINTS
    if not os.path.exists(FILE_COMPLAINTS):
        cols = ["order_id", "noidung"]
        pd.DataFrame(columns=cols).to_csv(FILE_COMPLAINTS, index=False, sep=';')
        print(f"✅ Đã tạo mới: {FILE_COMPLAINTS}")
    else:
        print(f"⏩ Đã có file {FILE_COMPLAINTS}")

    print("🎉 KIỂM TRA HOÀN TẤT.")

if __name__ == "__main__":
    create_data_final()