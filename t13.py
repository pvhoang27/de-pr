orders = [
    {"id": 101, "amount": "200"},
    {"id": 102},
    {"id": 103, "amount": "abc"},
    {"id": 104, "amount": "300"}
]

total = 0
error_count = 0

# M tự viết vòng lặp ở đây
for order in orders : 
    if order.get("amount") is None :
        error_count += 1
    else :
        try: 
            amount = int(order["amount"])
            if amount > 0 : total += amount 
            else : error_count += 1
        except (ValueError, TypeError):
            error_count += 1
print(total)
print(error_count)