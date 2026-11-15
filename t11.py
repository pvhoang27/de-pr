total = 0
value_errors = 0
type_errors = 0
invalid_amounts = 0
orders = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": "abc"},
    {"id": 103, "amount": None},
    {"id": 104, "amount": "-50"},
    {"id": 105, "amount": "300"}
]

# M tự viết vòng lặp ở đây
for order in orders: 
    try: 
        amount = int(order["amount"])
        if amount > 0 : 
            total += amount 
        else: 
            invalid_amounts += 1
    except ValueError:
        value_errors += 1
    except TypeError:
        type_errors += 1

print(total)
print(value_errors)
print(type_errors)
print(invalid_amounts)