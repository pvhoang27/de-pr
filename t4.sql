select d.product_name, sum(f.revenue) as total_revenue
from fact_sales as f 
join dim_product as d 
on d.product_id = f.product_id
group by product_name 
having sum(f.revenue) > 500
order by sum(f.revenue) desc 