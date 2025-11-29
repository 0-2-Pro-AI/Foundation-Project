food_list = []
address_list = []

def MENU():
    print (" Welcome to SEND2YOU shop!")
    print("1. Making your new order ")
    print("2. Checking your listing")
    print("3. Exit")

def order():
    food = input ("Your choice: ")
    address = input ("Delivery address: ")
    print("It`s added!")

    food_list.append(food)
    address_list.append(address)

def checking():
    print("---Your listings---" )
    for i in range():
        print(f"ID{i+1} | Food: {food_list(i)} | At: {address_list(i)}")

def main():
    while True:
        MENU()
        choice = input("Choose (1/2/3): ")

        if choice == 1:
            order()
        elif choice == 2:
            checking()
        elif choice == 3:
            break

main()