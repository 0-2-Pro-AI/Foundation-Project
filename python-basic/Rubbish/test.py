import pandas as pd
import os

FILE_CLIENT = "client.csv"
FILE_ODERS = "orders.csv"
FILE_PRODUCTS = "products.csv"
FILE_STAFF = "staff.csv"
FILE_COMPLAINT = "complaint.csv"

def all_orders ():
    if not os.path.exists(FILE_CLIENT):
        data_clients = {
            "ID": ["123","122"],
            "Name": ["Tong", "Eric"]
        }
        pd.DataFrame(data_clients).to_csv(FILE_CLIENT, index=False, sep=';')
        print("created")
    else:
        print("keep")

    if not os.path.exists(FILE_STAFF):
        delivery_data = {
            "password": ["12", "13"],
            "zone" :["west", "south"]
        }
        pd.DataFrame(delivery_data).to_csv(FILE_STAFF, index=False, sep=';')
        print("created")
    else:
        print("keep")

    if not os.path.exists(FILE_PRODUCTS):
        products_data ={
            "ID": ["102", "101"],
            "product": ["red", "blue"]
        }
        pd.DataFrame(products_data).to_csv(FILE_PRODUCTS, index=False, sep=';')
        print("created")
    else:
        print("keep")

    if not os.path.exists(FILE_ODERS):
        co =["id","client","delivery"]
        pd.DataFrame(columns=co).to_csv(FILE_ODERS, index=False, sep=';')
        print("created")
    else:
        print("keep")

    if not os.path.exists(FILE_COMPLAINT):
        sl= ["id client","content"]
        pd.DataFrame(columns=sl).to_csv(FILE_COMPLAINT, index=False, sep=';')
        print("created")
    else:
        print("keep")

    print("Done")

if __name__ == "__main__":
    all_orders()


