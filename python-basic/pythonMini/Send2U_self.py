orders = []
MENU_items = {
    "pizza": 3,
    "kebab": 4,
    "kfc": 5,
    "ham": 2
}

def MENU():
    print()
    print("="*30)
    print ("---Welcome to SEND2YOU shop!---")
    print("="*30)
    print("1. Making your new order ")
    print("2. Checking your listing")
    print("3. Exit")
    print("4. Delete order")

def order():
    print("\n---MAKING YOUR NEW ORDER--- ")
    food_name = ""
    price = 0
    while True:
        food_name = input("Your order: ").strip().lower()
        if food_name in MENU_items:
            price = MENU_items[food_name]
            print(f"Success! Your {food_name} is {price} euros")
            break
        else:
            print("We don`t have this option! Please try: ", list(MENU_items.keys()))

    address = input("Delivery address: ")
    duration = input("Delivery time: ")

    single_order = {
        "food": food_name,
        "price": price,
        "address": address,
        "duration": duration,
        "status": "Pendent"
    }
    orders.append(single_order)
    print("--> Orders saved successfully!")

def checking():
    print("\n---Your listings---" )

    if not orders:
        print("No order found")
    else:
        for i, order in enumerate(orders,1):
            print(f"ID: {i} | Your order:{order['food']} | Price:{order['price']} | Status:{order['status']}")
    
        print("-"*30)
        total = sum(order["price"] for order in orders)
        print(f"TOTAL BILL: {total} euros")

def delete():
    print("\n ---CANCEL ORDERS---")
    checking()
    while True:
        try:
            index = input("Enter ID to cancel(ex: 1,3) or '0' to back: ")
            if index == "0":
                print("--> Back to menu.")
                break

            id_str_list = index.split(",")
            valid_indexes = []

            for s in id_str_list:
                if s.strip():
                    idx = int(s.strip()) - 1
                    if 0 <= idx <len(orders):
                        valid_indexes.append(idx)

            if not valid_indexes:
                print("No valid IDs found! Please check your list again.")
                continue
           
            valid_indexes.sort(reverse=True)

            print(f"--> Deleting {len(valid_indexes)} item(s)...")
            for idx in valid_indexes:
                removed_item = orders.pop(idx)
                print(f" Deleted: {removed_item['food']}")

            print("--> Done.")

        except ValueError:
            print("Error! Please enter numbers separated by comma (1,2).")
    
         

def main():
    processing = True
    while processing:
        MENU()
        choice = input("Choose (1/2/3/4): ")
        if choice == "1":
            order()
        elif choice == "2":
            checking()
        elif choice == "3":
            print("Good bye!")
            break
        elif choice == "4":
            delete()

        else:
            print("Your choice is invalid!")

main()