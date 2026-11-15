valid_orders = []
error_orders = []
total = 0
orders = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": None},
    {"id": 103, "amount": "xyz"},
    {"id": 104, "amount": "400"},
    {"id": 105, "amount": -20},
    {"id": 106, "amount": "300"}
]

# M viết vòng lặp ở đây
for order in orders : 
    try:
        amount = int(order["amount"])
        if amount > 0 : 
            valid_orders.append(order)
            total += amount 

        else : 
            error_orders.append(order)
    except (ValueError, TypeError):
        error_orders.append(order)

print(len(valid_orders))
print(len(error_orders))
print(total)