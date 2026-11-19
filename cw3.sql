with xep as (
    select order_id, customer_id,amount
    row_number() over(
        partition by customer_id
        order by amount desc  ,customer_id asc
    ) as rn
)

select * from xep 
where rn = 1 

