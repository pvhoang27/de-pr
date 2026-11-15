orders = [
    {"id": 101, "customer": "An", "amount": 200},
    {"id": 102, "customer": "Bình", "amount": None},
    {"id": 103, "customer": "Cường", "amount": 300},
    {"id": 101, "customer": "An", "amount": 200},
    {"id": 104, "customer": "Dũng", "amount": 500}
]
result = []
seen_ids = set()

# for order in orders:
#     if order["id"] not in seen_ids:
#         if order["amount"] is not None:
#             result.append(order)
#             seen_ids.add(order["id"])


for order in orders:
    if order["amount"] is not None:
        if order["id"] not in seen_ids:
            result.append(order)
            seen_ids.add(order["id"])

print(len(result))