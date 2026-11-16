insert into orders(id, amount)
values (101, 250),
    (103,400)
on conflict(id)
do update set amount = excluded.amount;
