orders = [
    {"id": 1, "customer": " An ", "amount": "100"},
    {"id": 2, "customer": " Bình ", "amount": "200"},
    {"id": 3, "customer": " Cường ", "amount": "abc"}
]

valid_orders = []
error_orders = []
total = 0

# M tự viết code ở đây
bs = orders.copy()
# print(bs)

for a in bs : 
    a["customer"] = a["customer"].strip()
# print(bs)

for a in bs: 
    try :
        amount = int(a["amount"])
        a["amount"] = amount
        if amount > 0 : 
            total += amount
            valid_orders.append(a)
        else : 
            error_orders.append(a)
    except (ValueError, TypeError):
        error_orders.append(a)



print(len(valid_orders))
print(len(error_orders))
print(total)
print(orders[0])
print(valid_orders[0])