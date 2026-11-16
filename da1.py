orders = [
    {"id": 101, "amount": "200"},
    {"id": 102, "amount": "300"},
    {"id": 101, "amount": "500"},
    {"id": 103, "amount": None},
    {"id": 104, "amount": "-50"},
    {"id": 105, "amount": "abc"},
    {"id": 106, "amount": "150"}
]

valid_orders = []
error_orders = []
seen_ids = set()
total = 0 

for i in orders : 
    if i["id"] not in seen_ids : 
        try :
            amount = int(i["amount"])
            if amount > 0 : 
                valid_orders.append(i)
                i["amount"] = amount
                total += amount
                seen_ids.add(i["id"])
            else:
                error_orders.append(i)
        except (ValueError, TypeError):
            error_orders.append(i)
    else :
        error_orders.append(i)
print("Valid orders:", len(valid_orders))
print("Error orders:", len(error_orders))
print("Total revenue:", total)