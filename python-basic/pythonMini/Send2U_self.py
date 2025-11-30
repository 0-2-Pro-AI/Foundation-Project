food_list = []
status_list = []

def MENU():
    print ("\n Welcome to SEND2YOU shop!")
    print("1. Making your new order ")
    print("2. Checking your listing")
    print("3. Exit")

def order():
    print("\n Making your new order.")
    while True: 
        food = input ("Your choice: ")

        if len(food) > 0 : break
        print("Error! Please try again!")

    address = input ("Delivery address: ")
    duration = input ("Delivery time: ")
    info = f"{food}, From: SEND2U--->To:{address}[{duration}] "
    food_list.append(info)
    status_list.append("Pendent")
    print(f"Your {food} is on the status `Pendent`.")

def checking():
    print("---Your listings---" )

    if len(food_list) == 0:
        print("No oders found!")

    else :
        for i in range(len(food_list)):
            print(f"ID{i+1} | Food: {food_list[i]} | Status:{status_list[i]}")

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