def calculate_discount(quantity, price, discount_rate):
    total = quantity * price
    discount = total * discount_rate / 100
    final_price = total - discount
    return discount, final_price


quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (%): "))

discount, final_price = calculate_discount(quantity, price, discount_rate)

print("Discount amount: $", round(discount, 2))
print("Discounted price: $", round(final_price, 2))