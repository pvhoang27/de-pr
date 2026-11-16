orders = [
    {"id": 1, "amount": "200", "status": "completed"},
    {"id": 2, "amount": None, "status": "completed"},
    {"id": 3, "amount": "300", "status": "pending"},
    {"id": 4, "amount": "abc", "status": "completed"},
    {"id": 5, "amount": "150", "status": "completed"}
]


# bs = orders.copy()
valid_orders = []
error_orders = []
total = 0 

# for i in bs:
#     if i["status"] == "completed": 
#         try : 
#             amount = int(i["amount"])

#             if amount >  0 :
#                 i["amount"] = amount
#                 valid_orders.append(i)
#                 total += amount
#             else: 
#                 error_orders.append(i)
#         except (ValueError, TypeError):
#             error_orders.append(i)
#     else:  
#         error_orders.append(i)
# print("Valid:", len(valid_orders))  
# print("Error:", len(error_orders))
# print("revenue:", total)

# print(orders)
# print(bs)
# print("--------------------")
# print(valid_orders)


for i in orders:
    order = i.copy()

    if order["status"] == "completed":
        try:
            amount = int(order["amount"])

            if amount > 0:
                order["amount"] = amount
                valid_orders.append(order)
                total += amount
            else:
                error_orders.append(order)

        except (ValueError, TypeError):
            error_orders.append(order)
    else:
        error_orders.append(order)