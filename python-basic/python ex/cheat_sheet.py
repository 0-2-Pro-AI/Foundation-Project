# 1. Reform the "string"
# strip() delete the space before and after the input
# lower() small all letters to compare
food = input("Enter your name: ").strip().lower()

#2. Dictionary(fast search, use{})
menu = {
    "key": "value",
    "pizza": 5
}
# Take the price: menu["pizza"]

#3. List(contains many dict, use[])
orders = []
#add to list: orders.append(...)