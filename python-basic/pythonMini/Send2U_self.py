orders = ()
MENU_items = {
    "pizza": 3,
    "kebab": 4,
    "kfc": 5,
    "ham": 2
}

def MENU():
    print ("\n Welcome to SEND2YOU shop!")
    print("1. Making your new order ")
    print("2. Checking your listing")
    print("3. Exit")

def order():
    while True:
        print("\n---MAKING YOUR NEW ORDER--- ")
        food_name = input("Your order: ").lower
        if food_name in MENU_items():
            print(f"Success! Your {food_name} is {MENU_items[food_name]} euros")
            break
        else:
            print("We don`t have this option!")

        address = input("Delivery address: ")
        duration = input("Delivery time: ")

    single_order = {
        "food": food_name,
        "price": MENU_items[food_name],
        "address": address,
        "duration": duration,
        "status": "Pendent"
    }
    orders.append(single_order)

def checking():
    print("---Your listings---" )

    if not orders:
        print("No order found")
    else:
        for i, order in enumerate(orders,1):
            print(f"ID: {i} | Your order:{order["food"]} | Price:{order["price"]} | Status:{order["Pendent"]}")

def main():
    processing = True
    while processing == True:
        MENU()
        choice = input("Choose (1/2/3): ")

        if choice == "1":
            order()
        elif choice == "2":
            checking()
        elif choice == "3":
            print("Good bye!")
            break

        else:
            print("Your choice is invalid!")

main()