
tax_rate = 0.07


def calculate_total(quantity, price):
    subtotal = quantity * price
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total


quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

subtotal, tax, total = calculate_total(quantity, price)

print("Subtotal: $", round(subtotal, 2))
print("Tax: $", round(tax, 2))
print("Total price: $", round(total, 2))
