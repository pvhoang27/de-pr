import csv 
# extract 
with open("orders.csv","r") as f :
    orders = list(csv.DictReader(f))

#transform
clean =[]
for i in orders : 
    try:
        i["id"] = int(i["id"])
        amount = int(i["amount"])
        i["amount"] = amount 

        if amount > 0 :
            clean.append(i)
    except (ValueError, TypeError):
        pass

#load 
import sqlite3 
conn = sqlite3.connect("orders.db")

conn.execute("""
    create table if not exists orders (
        id integer primary key,
        amount integer
    )
""")

for i in clean:
    conn.execute(
        "insert into orders (id, amount) values (?, ?)",
        (i["id"], i["amount"])
    )

conn.commit()
conn.close()
