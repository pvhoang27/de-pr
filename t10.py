orders = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": "200"},
    {"id": 101, "amount": "100"},
    {"id": 103, "amount": "abc"},
    {"id": 104, "amount": None},
    {"id": 105, "amount": "300"}
]

valid_orders = []
error_orders = []
seen_ids = set()
total = 0

# M tự viết code ở đây
for order in orders : 
    if order["id"] not in seen_ids: 
        try :
            amount = int(order["amount"])
            valid_orders.append(order)
            total += amount
            seen_ids.add(order["id"])
        except (ValueError, TypeError):
            error_orders.append(order)
            seen_ids.add(order["id"])
    else: 
        error_orders.append(order)

print(len(valid_orders))
print(len(error_orders))
print(total)