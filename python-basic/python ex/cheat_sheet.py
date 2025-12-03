# 1. Reform the "string"
# strip() delete the space before and after the input
# lower() small all letters to compare
food = input("Enter your name: ").strip().lower()


# 2. Dictionary(fast search, use{})
menu = {
    "key": "value",
    "pizza": 5
}
# Take the price: menu["pizza"]


# 3. List(contains many dict, use[])
orders = []
#add to list: orders.append(...)


#4. Dicts in Dict( Big Tech )
orders = {
    "ID_101": {"food": "Pizza", "price":5},
    "ID_102": {"food": "Kebab", "price": 4},
    #....
    "ID_999999": {"food": "Pho", "price": 10}
}
# If we use list for search, it will run each ID from the beginning and imagine 
# when Meta has 3 billions users. It will take the whole day to search an info about you. O(3 billions)
# But with dicts, we can find your info in 1 second wherever the orden of info. O(1)


# 5. But is List is useless?
# No cause List have 3 major advantages compare with Hash
# First, it costs less RAM for the same data(vital for glass AI)
# Second, it keep the ordens ( perfect for playist or history)
# Third, it allows dupliates (frequency data,habits, summary,AI training
# (pictures is basically huge list of same or different numbers) )

# List often uses ordens data, image processing
# Dict use for the unique info(User ID, Menu,...)
# EX: Meta use List for New feeds, cause the ordens of post is sequentially
#     But for Database, it´s Hash Map (Dicts in Dict)


# 6. Condition funtion(try.except & if.else)
# try.except help to frame the type of data to avoid the program crashing, 
# if the info is not the right type of data, it come to except ValueError to warn the user to use the correct data
# if.else help to valid the data, is that satisfied the database or not 
try:
    index = int(input("Enter the ID you want to cancel: "))
    index = index - 1 
    if 0 <= index < len(orders):
        item = orders.pop(index)
        print(f"Your {item['food']} have been cancelled.")
    else:
        print(" Your ID is not valid. Please try again!")
except ValueError:
    print("Please enter a number.")


# 7. Loop(for.in & while.True/condition)
# "for.in" use to run through each element of the set, safe, use when you know exactly amount of elements
# and it will automatic stop when end of the list
# Ex: Run through the pixel in an image or the data folder

# "while" use to run the main permanent, just stop when satisfy a condition or break,
# it´s dangerous cause make the program is permanently suspended when make the wrong condition or forget the break,
# and we use it when don´t know exactly amount of elements
# Ex: Train AI continuosly until their error is low enough


# 8. While.True + try.except + .split + valid_indexes.sort(reverse=True) + dict.pop

def delete():
    print("\n--- CANCEL ORDER ---")
    # checking() # Hiện danh sách để khách thấy đường mà xóa
    
    while True:
        try:
            # 1. Nhập liệu (Vừa số đơn, vừa số nhiều, vừa lệnh thoát)
            raw_input = input("Enter IDs to cancel (e.g. 1,3) or '0' to back: ").strip()
            
            # 2. LỐI THOÁT HIỂM
            if raw_input == '0':
                print("--> Back to Menu.")
                break 
            
            # 3. XỬ LÝ CHUỖI -> DANH SÁCH INDEX
            # Kỹ thuật List Comprehension (Dân Pro hay dùng để viết gọn vòng lặp for)
            # Dòng dưới nghĩa là: Cắt chuỗi, strip từng cái, ép kiểu int, trừ đi 1
            # Chỉ lấy những index hợp lệ (nằm trong khoảng 0 đến len(orders))
            id_str_list = raw_input.split(",")
            valid_indexes = []
            
            for s in id_str_list:
                # Kiểm tra s có rỗng không (phòng trường hợp nhập "1,,2")
                if s.strip(): 
                    idx = int(s.strip()) - 1
                    if 0 <= idx < len(orders):
                        valid_indexes.append(idx)
            
            # 4. KIỂM TRA: Có xóa được cái nào không?
            if not valid_indexes:
                print("No valid IDs found! Please check checking() again.")
                continue # Quay lại đầu vòng lặp while
            
            # 5. SẮP XẾP GIẢM DẦN (Chống lỗi dồn toa)
            valid_indexes.sort(reverse=True)
            
            # 6. THỰC HIỆN XÓA
            print(f"--> Deleting {len(valid_indexes)} item(s)...")
            for idx in valid_indexes:
                removed_item = orders.pop(idx)
                print(f"    Deleted: {removed_item['food']}")
            
            print("--> Done.")
            # Có thể break để về menu luôn, hoặc bỏ break để xóa tiếp
            
        except ValueError:
            print("Error! Please enter numbers separated by comma (e.g. 1, 2).")


# 9. () & []
# [LIST], mutable (add, edit, delete)
# (TUPLE), immutable (fixed info like gps,facts,...)

# EX: ()call funtion run 
#   --> input(), print(),...

#     []search
#   --> orders[0], menu['food']

# TIPS PRO: 
# [LIST], use for same types of data
# (TUPLE), use for different types of data


# 10. When want to compare some info( words) from the user with the global variables,
# have to use function .strip().lower(), cause it will delete the space "" and small all
# the letter to easily compare with the global variables (avoid the crash just 
# because the differenc of small and big letters)

# But even for the info of numbers, .strip() is still vital, cause it prevent the "ghost space",
# EX: if the user enter the space " " in def update(), the memory will save it and it will 
#     replace the old info although the customer just want to pass this item. Then evidently, 
#     the shipper have no clue where to deliver the order in case of Uber


