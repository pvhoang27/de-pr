orders = [
    {"id": 1, "customer": " An ", "amount": "200"},
    {"id": 2, "customer": "  Bình  ", "amount": "300"},
    {"id": 3, "customer": " Cường ", "amount": "abc"},
    {"id": 4, "customer": " Dũng ", "amount": "400"}
]

valid_orders = []
error_orders = []
total = 0
clean = []

# M tự viết code ở đây
for order in orders : 
    name = order["customer"].strip()
    order["customer"] = name
    clean.append(order)

# for order in clean :
#     print(order)

for order in clean : 
    try:
         
        amount = int(order["amount"])
        order["amount"] = amount
        if amount > 0 : 
            total += amount
            valid_orders.append(order)
        else : 
            error_orders.append(order)
    except (ValueError, TypeError):
        error_orders.append(order)
    
    


print(len(valid_orders))
print(len(error_orders))
print(total)
print(valid_orders)