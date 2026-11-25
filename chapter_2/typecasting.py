a = 10;
b = "10"
print(a);
print(int(b) + 1);


def calculate_total(price, quantity):
    price = float(price)
    quantity = int(quantity)
    total = price * quantity
    return str(total)

product_price = "199.50"
product_quantity = "3"

result = calculate_total(product_price, product_quantity)

print("Total Amount: ₹" + result)
print(type(result))