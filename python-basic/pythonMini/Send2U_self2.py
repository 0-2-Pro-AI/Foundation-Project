orders = []
menu_items ={
    "pizza": 2,
    "kebab": 3,
    "ham": 3,
    "kfc": 4
}

def order_food():
    
    while True:
        print(f"This is our MENU, {menu_items}")
    
        food = input("Your food: ").strip().lower()

        if food in menu_items:
            price = menu_items[food]
            print(f" --> Success! Your {food}( {price} euros) is added in the shopping cart!")
            break
        else:
            print(f"Error! Your food is not valid! Try again!")
            continue

    while True:
        address = input("Delivery address: ").strip()
        if not address:
            print("Error! Please do not leave blank.")
            continue
        else:
            print("Your address is added.")
            break

    while True:
        duration = input("Delivery time( Ex: 15h-17h): ").strip()
        if not duration:
            print("Error! Please do not leave blank.")
            continue
        else:
            print("Your delivery time is added.")
            break

    single_order ={
        "food": food,
        "price": price,
        "address": address,
        "duration": duration,
        "status": "Pendent"
    }

    orders.append(single_order)
    print("Your orders saved successfully.")


def checking():
    print("\n ---Your listing---")

    if not orders:
        print("No orders found!")
    else:
        for i, order in enumerate(orders,1):
            print(f"Your ID: {i} | Food: {order['food']} | Price: {order['price']} | Status: {order['status']} ")

        print("-"*30)
        total = sum(order["price"] for order in orders )
        print(f"TOTAL BILL: {total} euros. ")


 def update():
    print("\n ---UPDATE YOUR ORDER---")
    checking()
    
    while True:
        try:
            user_id = input("Please enter your ID (or '0' to come back): ").strip()
            
            if user_id == "0":
                print("--> Back to the menu.")
                break
            
            real_id = int(user_id - 1)
            if not 0 <= real_id < len(orders):
                print("Error! Please enter a valid ID.")
                continue

            current_order = orders[real_id]

            while True:
                print("\n ---UPDATE YOUR ORDERS---")
                print(f"Food: ")

            



                










    










def main():
    while True:
        print("\n ---Welcome to Send2You Shop---")
        print("1. Make you new order")
        print("2. Checking your listing")
        print("3. Update your order")
        print("4. Delete your orders")
        print("5. Exit")

        