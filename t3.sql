select d.product_name , sum(f.revenue) as total_revenue
from fact_sales as f 
join dim_product as d
on f.product_id = d.product_id
group by d.product_name