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


#4. Dicts in Dict( Big Tech )
orders = {
    "ID_101": {"food": "Pizza", "price":5},
    "ID_102": {"food": "Kebab", "price": 4},
    #....
    "ID_999999": {"food": "Pho", "price": 10}
}
# If we use list for search, it will run each ID from the beginning and imagine when Meta has 3 billions users. It will take the whole day to search an info about you. O(3 billions)
# But with dicts, we can find your info in 1 second wherever the orden of info. O(1)


#5. But is List is useless?
# No cause List have 3 major advantages compare with Hash
# First, it costs less RAM for the same data(vital for glass AI)
# Second, it keep the ordens ( perfect for playist or history)
# Third, it allows dupliates (frequency data,habits, summary,AI training(pictures is basically huge list of same or different numbers) )

# List often uses ordens data, image processing
# Dict use for the unique info(User ID, Menu,...)
# EX: Meta use List for New feeds, cause the ordens of post is sequentially
#     But for Database, it´s Hash Map (Dicts in Dict)