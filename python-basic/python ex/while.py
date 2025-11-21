food_order = []

print("---Welcome to send2you shop---")
print("Please choose your food, click Done when you´ve finished")

while True:
    new_dish = input("Your choice: ")
    if new_dish == "Done":
        break
    food_order.append(new_dish)
    print("It´s added:", new_dish)

print("---Your order---")
print(food_order)