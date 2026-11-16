select order_id, customer_id,amount, 
    row_number() over(
        partition by customer_id
        order by amount desc  
    ) as rn 
from orders 
order by customer_id desc 