orders = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": "200"},
    {"id": 101, "amount": "100"},
    {"id": 103, "amount": "abc"},
    {"id": 104, "amount": None},
    {"id": 105, "amount": "300"}
]

valid_orders = []
error_orders = []
seen_ids = set()
total = 0
order_unique = []

# M tự viết code ở đây
for order in orders : 
    if order["id"] not in seen_ids: 
        try : 
            amount = int(order["amount"])
            valid_orders.append(order)
            total += amount 
            seen_ids.add(order["id"])

        except (ValueError, TypeError):
            error_orders.append(order)
            seen_ids.add(order["id"])

#t se lam tuong minh
# for order in orders: 
#     if order["id"] not in seen_ids : 
#         seen_ids.add(order["id"])
#         order_unique.append(order)
# for order in order_unique : 
#     print(order)


# for order in order_unique: 
#     try :
#         amount = int(order["amount"])
#         if amount  > 0 : 
#             valid_orders.append(order)
#             total += amount
#         else :
#             error_orders.append(order)

#     except(ValueError, TypeError):
#         error_orders.append(order)

# for order in valid_orders :
#     print(order)

print(len(valid_orders))
print(len(error_orders))
print(total)