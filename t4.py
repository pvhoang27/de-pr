orders = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": "250"},
    {"id": 103, "amount": 300},
    {"id": 104, "amount": "150"}
]

total = 0
count = 0

# M tự viết vòng lặp ở đây
for order in orders : 
    amount = int(order["amount"])
    total += amount

    if amount > 200:
        count += 1

print(total)
print(count)