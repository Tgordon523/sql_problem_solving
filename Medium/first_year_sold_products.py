import duckdb

"""
Problem:

Select results for the first year a product was sold
"""

sql_init = """
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar);
Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values (1, 100, 2008, 10, 5000);
insert into Sales (sale_id, product_id, year, quantity, price) values (2, 100, 2009, 12, 5000);
insert into Sales (sale_id, product_id, year, quantity, price) values (7, 200, 2011, 15, 9000);
Truncate table Product;
insert into Product (product_id, product_name) values (100, 'Nokia');
insert into Product (product_id, product_name) values (200, 'Apple');
insert into Product (product_id, product_name) values (300, 'Samsung');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           SELECT S.product_id, S.year as first_year, S.quantity, S.price
           FROM 
           Sales S 
        RIGHT JOIN
           (
           SELECT
           S1.product_id, MIN(S1.year) as year
           FROM Sales S1
           GROUP BY product_id
           ) first_yr ON S.product_id=first_yr.product_id AND S.year=first_yr.year
            """).show()