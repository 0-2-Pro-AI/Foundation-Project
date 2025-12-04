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

    status = "Pendent"
    print("Status of your order is 'Pendent'!")

    single_order ={
        "food": food,
        "price": price,
        "address": address,
        "duration": duration,
        "status": status
    }

    orders.append(single_order)


def checking():
    print("\n ---Your listing---")
    for i in orders()








    










def main():
    while True:
        print("\n ---Welcome to Send2You Shop---")
        print("1. Make you new order")
        print("2. Checking your listing")
        print("3. Update your order")
        print("4. Delete your orders")
        print("5. Exit")

        