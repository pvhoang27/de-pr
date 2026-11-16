with xep(
    select order_id, customer_id, amount
    row_number() over(
        partition by customer_id
        order by amount desc
    ) as rn
)

select * from xep 
where rn = 1 
order by customer_id asc 