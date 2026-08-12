def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express": 
        cost = 20
    elif shipping_speed == "overnight":
        cost = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        cost = 0
    elif shipping_speed == "standard" and cart_total < 100:
        cost = 10
    else:
        print("Error! Invalid input for shipping speed. Please enter 'express', 'overnight', or 'standard'.")
        cost = 0
    return cart_total + cost

print(calculate_checkout(67, "express"))
