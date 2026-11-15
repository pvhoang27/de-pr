orders = [
    {"id": 1, "customer": " An ", "amount": 200},
    {"id": 2, "customer": " Bình ", "amount": -50},
    {"id": 3, "customer": " Cường ", "amount": None},
    {"id": 1, "customer": "An", "amount": 200},
    {"id": 4, "customer": " Dũng ", "amount": 400},
    {"id": 5, "customer": " Hà ", "amount": 0}
]

result = []
seen_ids = set()
total = 0

# M tự viết code xử lý ở đây
for order in orders : 
    if order["amount"] is not None and order["amount"] > 0 :
        if order["id"] not in seen_ids : 
            result.append(order)
            seen_ids.add(order["id"])
            total += order["amount"]
            

print(len(result))
print(total)