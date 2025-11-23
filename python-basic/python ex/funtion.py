order_list = []
price_list = []

def menu():
    print("\n---MENU SEND2YOU---")
    print("1.Make your order.")
    print("2.Your lists.")
    print("3.Exit.")

def make_your_order():
    order = input("Enter your choose: ")
    price = float(input("Enter the price: "))

    order_list.append(order)
    price_list.append(price)
    print(f"{order} is added.")

def your_list():
    print("---Your listing---")
    total_price = 0
    for i in range(len(order_list)):
        print(f"{i+1}: {order_list[i]} - Price: {price_list[i]}")
        total_price = total_price + price_list[i]

    print("-----------")
    print("TOTAL BILL: ", total_price)

while True:
    menu()
    choose = input("Please enter (1/2/3): ")
    if choose == "1":
        make_your_order()
    elif choose == "2":
        your_list()
    elif choose == "3":
        print("Good bye!")
        break
    else:
        print("Wrong choice!")









    
