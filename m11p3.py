
def calculate_sales(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    target = sales * 1.05
    return commission, target


last_name = input("Enter salesperson's last name: ")
sales = float(input("Enter sales amount: "))

commission, target = calculate_sales(sales)

print("Salesperson:", last_name)
print("Commission: $", round(commission, 2))
print("Next year's target: $", round(target, 2))
