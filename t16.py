orders = [
    {"id": "1", "amount": "100"},
    {"id": "2", "amount": "200"},
    {"id": "3", "amount": "300"}
]

total = 0

# M tự viết vòng lặp ở đây
for i in orders : 
    total += int(i["amount"])

print(total)