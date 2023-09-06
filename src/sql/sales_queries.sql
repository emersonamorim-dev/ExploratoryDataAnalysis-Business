-- Obter total de vendas por produto
SELECT product_id, product_name, SUM(quantity_sold) as total_sold
FROM sales_table
GROUP BY product_id, product_name
ORDER BY total_sold DESC;

-- Obter vendas mensais
SELECT 
    YEAR(sale_date) as sale_year, 
    MONTH(sale_date) as sale_month, 
    SUM(total_sale_amount) as monthly_sales
FROM sales_table
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;

-- Produtos mais vendidos no último mês
SELECT product_id, product_name, SUM(quantity_sold) as total_sold
FROM sales_table
WHERE sale_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE()
GROUP BY product_id, product_name
ORDER BY total_sold DESC LIMIT 10;

-- Vendas por categoria de produto
SELECT category, SUM(total_sale_amount) as total_sales
FROM sales_table
JOIN products_table ON sales_table.product_id = products_table.id
GROUP BY category
ORDER BY total_sales DESC;
