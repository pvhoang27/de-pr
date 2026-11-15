orders = [
    {"id": 101, "customer": "  An  ", "amount": 200},
    {"id": 102, "customer": " Bình ", "amount": None},
    {"id": 103, "customer": " Cường ", "amount": 300},
    {"id": 101, "customer": "An", "amount": 200},
    {"id": 104, "customer": " Dũng  ", "amount": 500}
]

result = []
seen_ids = set()
total = 0

# M tự viết phần for + if + strip + append + add + total
for order in orders:
    order["customer"] = order["customer"].strip()
# for order in orders:
#     print(order)
for order in orders : 
    if order["amount"] is not None :
        if order["id"]  not in seen_ids : 
            result.append(order)
            seen_ids.add(order["id"])
            total += order["amount"]



print(len(result))
print(total)