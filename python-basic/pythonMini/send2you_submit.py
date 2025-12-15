import time

orders = []
menu_items = {
    "pizza": 2,
    "kebab": 3,
    "ham": 3,
    "kfc": 4
}

def order_food():
    print("\n--- NEW ORDER ---")
    
    print("MENU AVAILABLE:")
    for item, price in menu_items.items():
        print(f" - {item.title()}: {price} euros")

    while True:
        food = input("Choose your food: ").strip().lower()
        if food in menu_items:
            price = menu_items[food]
            break
        print("Error: Item not in menu! Please try again.")

    while True:
        address = input("Delivery address: ").strip()
        if address:
            break
        print("Error: Address cannot be empty.")

    while True:
        duration = input("Delivery time (e.g., 15h-17h): ").strip()
        if duration:
            break
        print("Error: Time cannot be empty.")

    single_order = {
        "food": food,
        "price": price,
        "address": address,
        "duration": duration,
        "status": "Pending"  
    }

    orders.append(single_order)
    print(f"--> Success! {food.title()} added. Status: Pending.")


def checking():
    print("\n--- YOUR ORDERS ---")
    if not orders:
        print("No orders found.")
        return

    print(f"{'ID':<5} {'Food':<10} {'Price':<10} {'Status':<12} {'Address'}")
    print("-" * 60)
    
    total = 0
    for i, order in enumerate(orders, 1):
        print(f"{i:<5} {order['food'].title():<10} {order['price']:<10} {order['status']:<12} {order['address']}")
        total += order['price']
    
    print("-" * 60)
    print(f"TOTAL BILL: {total} euros")



def update():
    checking()
    if not orders:
        return

    while True:
        try:
            user_input = input("\nEnter ID to update (or '0' to cancel): ").strip()
            if user_input == '0':
                return
            
            real_id = int(user_input) - 1
            if 0 <= real_id < len(orders):
                current_order = orders[real_id]
                
        
                if current_order['status'] == "Confirmed":
                    print("Error: You cannot edit a confirmed order!")
                    continue

                print(f"\nEditing Order ID {user_input}:")
                print("1. Food")
                print("2. Address")
                print("3. Time")
                print("0. Back")
                
                choice = input("What do you want to change? ")

                if choice == "1":
                    print("Menu:", list(menu_items.keys()))
                    new_food = input("New food: ").strip().lower()
                    if new_food in menu_items:
                        current_order['food'] = new_food
                        current_order['price'] = menu_items[new_food]
                        print("--> Food updated.")
                    else:
                        print("Invalid food item.")

                elif choice == "2":
                    new_addr = input("New address: ").strip()
                    if new_addr:
                        current_order['address'] = new_addr
                        print("--> Address updated.")

                elif choice == "3":
                    new_time = input("New time: ").strip()
                    if new_time:
                        current_order['duration'] = new_time
                        print("--> Time updated.")

                elif choice == "0":
                    break
                else:
                    print("Invalid option.")
            else:
                print("Error: Invalid ID.")
        except ValueError:
            print("Error: Please enter a number.")


def delete():
    checking()
    if not orders:
        return

    try:
        user_input = input("\nEnter ID to delete (or '0' to cancel): ").strip()
        if user_input == '0':
            return

        real_id = int(user_input) - 1
        if 0 <= real_id < len(orders):
            removed = orders.pop(real_id)
            print(f"--> Order '{removed['food']}' deleted successfully.")
        else:
            print("Error: Invalid ID.")
    except ValueError:
        print("Error: Please enter a numeric ID.")


def confirm_order():
    print("\n--- CONFIRM ORDER ---")
    checking()
    if not orders:
        return

    try:
        user_input = input("\nEnter ID to CONFIRM (or '0' to cancel): ").strip()
        if user_input == '0':
            return
        
        real_id = int(user_input) - 1
        if 0 <= real_id < len(orders):
            if orders[real_id]['status'] == "Confirmed":
                print(f"Order #{user_input} is already confirmed.")
            else:
                orders[real_id]['status'] = "Confirmed"
                print(f"--> Success! Order #{user_input} is now CONFIRMED.")
        else:
            print("Error: ID not found.")
    except ValueError:
        print("Error: Please enter a valid number.")


def show_statistics():
    print("\n--- STATISTICS ---")
    if not orders:
        print("No data available.")
        return

    total_orders = len(orders)
    total_income = sum(o['price'] for o in orders)
    confirmed_count = sum(1 for o in orders if o['status'] == "Confirmed")
    pending_count = total_orders - confirmed_count

    print(f"Total Orders:      {total_orders}")
    print(f"Total Revenue:     {total_income} euros")
    print(f"Confirmed Orders:  {confirmed_count}")
    print(f"Pending Orders:    {pending_count}")
    input("\nPress Enter to continue...")



def main():
    while True:
        print("\n" + "="*30)
        print(" WELCOME TO SEND2YOU SHOP ")
        print("="*30)
        print("1. Create New Order")
        print("2. View Orders (List)")
        print("3. Update Order Details")
        print("4. Confirm Order Status") 
        print("5. Delete Order")
        print("6. View Statistics")       
        print("0. Exit")
        
        choice = input("Select option: ").strip()

        if choice == "1":
            order_food()
        elif choice == "2":
            checking()
            input("\nPress Enter to continue...")
        elif choice == "3":
            update()
        elif choice == "4":
            confirm_order()
        elif choice == "5":
            delete()
        elif choice == "6":
            show_statistics()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()