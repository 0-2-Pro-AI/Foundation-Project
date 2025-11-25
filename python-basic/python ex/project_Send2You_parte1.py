food_list = []
status_list = []

def MENU():
    print("\n"+"="*30)
    print("   SEND2YOU - CLIENT GATE   ")
    print("="*30)
    print("1. Make your new order")
    print("2. Check your listing")
    print("3. Exit")

def make_your_new_order():
    print("\n---- MAKING YOUR NEW ORDER ----")

    while True:
        food = input("Your order: ")
        if len(food) > 0 : break
        print("Error: Please enter your order!")
    
    address = input("Delivery address: ")
    duration = input("Delivery time( Ex: 17h -20h ): ")

    info = f"{food} | From: SEND2YOU SHOP --> To: {address}[{duration}]"
    food_list.append(info)

    status_list.append("Pendent")
    print(f"Success! {food} order is in status `Pendent`.")

def check_your_listing():
    print("\n ---- MY ORDERS ----")

    if len(food_list) == 0:
        print("No orders found.")

    else:
        for i in range(len(food_list)):
            print(f"ID {i+1} | {food_list[i]} | Status: {status_list[i]}")
            

def main():
    processing = True

    while processing == True:
        MENU()
        choices = input("Please enter (1/2/3): ")

        if choices == "1":
            make_your_new_order()
        elif choices == "2":
            check_your_listing()
        elif choices == "3":
            print("Good bye!")
            break

        else:
            print("Your choice is invalid! Please try again!")

main()