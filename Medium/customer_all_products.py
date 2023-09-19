import duckdb

"""
Problem: 
Select customers who have selected all products from the catalog
"""

sql_init = """
Create table If Not Exists Customer (customer_id int, product_key int);
Create table Product (product_key int);
Truncate table Customer;
insert into Customer (customer_id, product_key) values (1, 5);
insert into Customer (customer_id, product_key) values (2, 6);
insert into Customer (customer_id, product_key) values (3, 5);
insert into Customer (customer_id, product_key) values (3, 6);
insert into Customer (customer_id, product_key) values (1, 6);
Truncate table Product;
insert into Product (product_key) values (5);
insert into Product (product_key) values (6);
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           SELECT customer_id
           FROM 
           Customer c
           GROUP BY customer_id 
           HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product)
            """).show()