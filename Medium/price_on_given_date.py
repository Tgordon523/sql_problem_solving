import duckdb

"""
Problem:

Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.
"""

sql_init = """
Create table If Not Exists Products (product_id int, new_price int, change_date date);
Truncate table Products;
insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           WITH latest_price AS (
           SELECT
           RANK () OVER (PARTITION BY product_id ORDER BY change_date DESC) rank, 
           change_date, product_id, SUM(new_price) new_price
           FROM Products p
           GROUP BY product_id, change_date
           HAVING change_date <= '2019-08-16'
           )

           SELECT p2.product_id, COALESCE(lp.new_price, 10) latest_price
           FROM (SELECT DISTINCT p1.product_id FROM Products p1) p2 
           LEFT JOIN latest_price lp ON lp.product_id=p2.product_id and lp.rank = 1
            
           --WHERE rank=1
            """).show()

