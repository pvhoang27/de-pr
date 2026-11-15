orders = [
    {"id": 1, "customer": "An", "amount": "200"},
    {"id": 2, "customer": "Bình", "amount": "abc"},
    {"id": 3, "customer": "Cường", "amount": "300"},
    {"id": 4, "customer": "Dũng", "amount": "xyz"}
]

valid_orders = []
error_orders = []

# M tự viết vòng lặp try/except ở đây
for order in orders:
    try: 
        amount = int(order["amount"])
        valid_orders.append(order)
    except ValueError:
        error_orders.append(order)

print(len(valid_orders))
print(len(error_orders))
print(valid_orders[1]["amount"])