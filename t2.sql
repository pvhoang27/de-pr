select d.product_name, f.quantity, f.revenue
from fact_sales as f 
join dim_product as d 
on f.product_id = d.product_id