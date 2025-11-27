guest_list = []

print("----GUEST FOR PARTY(maximum 8)----")

for i in range(8):
    new_name = input(f"Enter the name of {i+1} person (or type `finish` to stop): ")
    if new_name == "finish":
        print("-> The list is full")
        break

    guest_list.append(new_name)

print("---Final list---")
print(guest_list)