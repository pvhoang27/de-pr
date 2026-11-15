orders = [
    {"id": 101, "amount": "200"},
    {"id": 102, "amount": "abc"},
    {"id": 103, "amount": "400"},
    {"id": 104, "amount": "xyz"},
    {"id": 105, "amount": "100"}
]

total = 0
error_count = 0

for order in orders:
    try:
        amount = int(order["amount"])
        total += amount
    except ValueError:
        error_count += 1

print(total)
print(error_count)