import pandas as pd
import os

FILE_CLIENTS = "login_client.csv"
FILE_STAFF = "works_delivery.csv"
FILE_PRODUCTS = "products_stock.csv"
FILE_ORDERS = "orders.csv"
FILE_COMPLAINTS = "complaints.csv"

def all_users_log_in():
    all_users = []

    if os.path.exists(FILE_CLIENTS):
        try:
            df=pd.read_csv(FILE_CLIENTS, dtype=str, sep=';')
            for _, row in df.iterrows():
                all_users.append({
                    "id": str(row['Contact']),
                    "pass": str(row['Password']),
                    "role": 'customer',
                    "name": str(row['name'])
                })
        except Exception as e:
            print(f"Error in reading file client :{e}")

    if os.path.exists(FILE_STAFF):
        try:
            df = pd.read_csv(FILE_STAFF, dtype=str, sep=';')
            for _, row in df.iterrows():
                user_role= "tarefa"
                if "Gestor" in str(row['zone']):
                    user_role = "manager"
                all_users.append({
                    "id": str(row["Login"]),
                    "pass": str(row["Password"]),
                    "role": user_role,
                    "name": str(row["Login"])
                })
        except Exception as e:
            print(f"Error in reading staff file: {e}")

        return pd.DataFrame(all_users)
    
def load_products():
    if os.path.exists(FILE_PRODUCTS):
        df =pd.read_csv(FILE_PRODUCTS, dtype=str, sep=';', encoding='utf-8-sig')
        if "Unnamed: 0" in df.columns:
            df=df.drop(columns=["Unnamed: 0"])
        return df
    return pd.DataFrame(columns=['Id','Product','Quantity in stock','Unit price'])

def save_products(df):
    df.to_csv(FILE_PRODUCTS, index=False, sep=';', encoding='utf-8-sig')