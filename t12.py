orders = [
    {"id": 1, "amount": "150"},
    {"id": 2, "amount": "abc"},
    {"id": 3, "amount": None},
    {"id": 4, "amount": "250"},
    {"id": 5, "amount": "-20"},
    {"id": 6, "amount": "xyz"}
]

total = 0
value_errors = 0
type_errors = 0
invalid_amounts = 0

# M tự viết code ở đây
for order in orders: 
    try :
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