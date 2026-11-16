select c.name, sum(o.amount) as total_amount
from orders as o 
join customers as c 
on o.customer_id = c.customer_id
group by c.name
having sum(o.amount) >= 500
order by sum(o.amount) desc