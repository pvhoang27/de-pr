data = {
    "status": "success",
    "orders": [
        {"id": 101, "amount": "200", "status": "completed"},
        {"id": 102, "amount": "300", "status": "pending"},
        {"id": 103, "amount": "150", "status": "completed"},
        {"id": 104, "amount": "400", "status": "cancelled"}
    ]
}

total = 0 
count = 0 

for i in data["orders"]:
    if i["status"] == "completed":
        total += int(i["amount"])
        count += 1
print("Completed orders:" , count)
print("Total revenue:", total)