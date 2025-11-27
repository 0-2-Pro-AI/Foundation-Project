food_list = ["Pizza", "Kebab", "KFC", "Donut", "Chips"]
price_list = [2, 3.4, 1.3, 9.3, 5.6]
status_list = ["conclude","pendent","cancel","conclude","pendent"]

print("---Revenue of Send2You---")
total_revenue = 0
total_waitlist = 0
max_price = 0


for i in range(len(food_list)):
    food = food_list[i]
    price = price_list[i]
    status = status_list[i]

    if status == "conclude":
        total_revenue = total_revenue + price

    if status == "pendent":
        total_waitlist = total_waitlist + 1
        print(f"Warn: The {food} are still not conclude")

    if price > max_price:
        max_price = price

print("-----------------")
print(".....Total revenue.....")
print("Final revenue: ", total_revenue)
print("Total pending order: ", total_waitlist)
print("The most expensive food: " , max_price)
