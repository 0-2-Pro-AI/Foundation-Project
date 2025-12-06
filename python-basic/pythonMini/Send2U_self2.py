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
            
            real_id = int(user_id) - 1
            if not 0 <= real_id < len(orders):
                print("Error! Please enter a valid ID.")
                continue

            current_order = orders[real_id]

            while True:
                print("\n ---UPDATE YOUR ORDERS---")
                print(f"1. Food: {current_order['food']} | Price: {current_order['price']} euros.")
                print(F"2. Delivery address: {current_order['address']}")
                print(f"3. Delivery time: {current_order['duration']}")
                print(f"0. Save and exit")

                choice = input("Please enter 1/2/3/0: ").strip()
                if choice == "0":
                    print("Your updated have successfully done!")
                    break
                
                elif choice == "1":
                    print("Menu:", list(menu_items.keys()))
                    new_order = input("Your new order:").strip().lower()
                    if new_order in menu_items:
                        current_order['food'] = new_order
                        current_order['price'] = menu_items[new_order]
                        print(f"Your new order {new_order} is {current_order['price']} euros")
                    else:
                        print("Your foood is not in the menu!")
                        continue

                elif choice == "2":
                    new_address = input("Delivery address:").strip()
                    if new_address:
                        current_order["address"] = new_address
                        print("Your address has successfully updated!")
                    else:
                        print("Don't leave blank.")

                elif choice == "3":
                    new_duration = input("Delivery time(ex: 17-19h): ").strip()
                    if new_duration:
                        current_order["duration"] = new_duration
                        print("--> Time updated.")
                    else: 
                        print("Don't leave blank.")

                else:
                    print("Please enter 1/2/3/0: ")

        except ValueError:
            print("Please enter a number!")
            continue

def delete():
    print("\n ---Cancel Orders---")
    checking()
    while True:
        try:
            user_id = input("Enter the ID (ex:1,3 or '0' to come back): ")
            if user_id == "0":
                print("--> Back to the menu")
                break

            id_list = user_id.split(",")
            valid_id = []

            for s in id_list:
                if s.strip():
                    idx = int(s.strip()) - 1
                    if 0 <= idx < len(orders):
                        valid_id.append(idx)

            if not valid_id:
                print("No valid ID.")
                continue

            valid_id.sort(reverse=True)
            print(f"--> Deleting {len(valid_id)} items...")
            
            for idx in valid_id:
                removed = orders.pop(idx)
                print(f"Deleted: {removed['food']}")
                print("--> Done")

            checking()
            
        except ValueError:
            print("Error!")
                    

            

def MENU():
    
    print("\n ---Welcome to Send2You Shop---")
    print("="*30)
    print("1. Make you new order")
    print("2. Checking your listing")
    print("3. Update your order")
    print("4. Delete your orders")
    print("5. Exit")


def main():
    while True:
        MENU()
        choice = input ("Choose 1/2/3/4/5: ")
        if choice == "5":
            print("Good bye.")
            break
        elif choice == "1":
            order_food()
        elif choice == "2":
            checking()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()

        else: 
            print("Your choice is invalid!")
main()    