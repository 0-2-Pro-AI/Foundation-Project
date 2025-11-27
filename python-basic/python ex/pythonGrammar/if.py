total_bill = float(input("Insert the total bill:"))
shipping_fee = 0

if total_bill >= 50:
    print("You´ve got free ship")
    shipping_fee = 0

else:
    print("Small order, shipping fee is 5 euro.")
    shipping_fee = 5

counting_bill = total_bill + shipping_fee

print("---Bill---")
print("Price of product:", total_bill)
print("Shipping fee:", shipping_fee)
print("TOTAL:", counting_bill)