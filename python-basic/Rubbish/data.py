import pandas as pd
import os

# Cấu hình tên file
FILE_CLIENTS = "login_client.csv"
FILE_STAFF = "works_delivery.csv"
FILE_PRODUCTS = "products_stock.csv"
FILE_ORDERS = "orders.csv"
FILE_COMPLAINTS = "complaints.csv"

# --- HÀM 1: GOM USER (QUAN TRỌNG NHẤT) ---
def load_all_users_for_login():
    """
    Đọc file Client và Staff (dùng dấu chấm phẩy),
    Gộp lại thành 1 danh sách chuẩn [id, pass, role, name]
    """
    all_users = []

    # A. Đọc Clients
    if os.path.exists(FILE_CLIENTS):
        try:
            # sep=';' và dtype=str là bắt buộc
            df = pd.read_csv(FILE_CLIENTS, sep=';', dtype=str)
            for _, row in df.iterrows():
                all_users.append({
                    "id": str(row["Contact"]),   # ID là SĐT
                    "pass": str(row["Password"]),
                    "role": "client",            # Gán cứng role Client
                    "name": str(row["Name"])
                })
        except Exception as e:
            print(f"⚠ Lỗi đọc Client: {e}")

    # B. Đọc Staff
    if os.path.exists(FILE_STAFF):
        try:
            df = pd.read_csv(FILE_STAFF, sep=';', dtype=str)
            for _, row in df.iterrows():
                # Phân tích Role dựa vào Zone
                user_role = "estafeta" # Mặc định là shipper
                if "Gestor" in str(row["Zone"]):
                    user_role = "manager" # Nếu Zone là Gestor thì là Admin
                
                all_users.append({
                    "id": str(row["Login"]),     # ID là Login
                    "pass": str(row["Password"]),
                    "role": user_role,
                    "name": str(row["Login"])    # Lấy Login làm tên tạm
                })
        except Exception as e:
            print(f"⚠ Lỗi đọc Staff: {e}")

    return pd.DataFrame(all_users)

# --- HÀM 2: SẢN PHẨM ---
def load_products():
    if os.path.exists(FILE_PRODUCTS):
        return pd.read_csv(FILE_PRODUCTS, sep=';', dtype=str) # Đọc str để giữ giá "3,00"
    return pd.DataFrame()

def save_products(df):
    df.to_csv(FILE_PRODUCTS, index=False, sep=';')

# --- HÀM 3: ĐƠN HÀNG ---
def load_orders():
    if os.path.exists(FILE_ORDERS):
        return pd.read_csv(FILE_ORDERS, sep=';', dtype=str)
    return pd.DataFrame(columns=["order_id", "client_id", "product_id", "status", "shipper_id"])

def save_orders(df):
    df.to_csv(FILE_ORDERS, index=False, sep=';')

# --- HÀM 4: KHIẾU NẠI ---
def load_complaints():
    if os.path.exists(FILE_COMPLAINTS):
        return pd.read_csv(FILE_COMPLAINTS, sep=';', dtype=str)
    return pd.DataFrame(columns=["order_id", "noidung"])

def save_complaints(df):
    df.to_csv(FILE_COMPLAINTS, index=False, sep=';') 
    