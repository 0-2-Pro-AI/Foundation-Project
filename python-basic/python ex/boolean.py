food_list = []
processing = True

print("Please enter your food (type Done to finish)")

while processing == True:

    food = input("Enter your food: ")
    if food == "Done":
        processing = False

    else: 
        food_list.append(food)
        print("It´s added: ", food)

print("Your order: ", food_list)
