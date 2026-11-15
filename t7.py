order = {
    "id": 101,
    "amount": "500"
}

amount = int(order["amount"])

print(type(order["amount"]))
print(type(amount))

order["amount"] = amount

print(type(order["amount"]))