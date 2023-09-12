import duckdb

"""
Problem:
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers
"""

sql_init = """
Create table If Not Exists Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date);
Truncate table Delivery;
insert into Delivery values (1, 1, '2019-08-01', '2019-08-02');
insert into Delivery values (2, 2, '2019-08-02', '2019-08-02');
insert into Delivery values (3, 1, '2019-08-11', '2019-08-12');
insert into Delivery values (4, 3, '2019-08-24', '2019-08-24');
insert into Delivery values (5, 3, '2019-08-21', '2019-08-22');
insert into Delivery values (6, 2, '2019-08-11', '2019-08-13');
insert into Delivery values (7, 4, '2019-08-09', '2019-08-09');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           WITH first_date AS
           (
           SELECT *,
           (CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END) logic,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) rank
           FROM Delivery D 
           --WHERE 
           )

           SELECT SUM(logic)/ COUNT(*) immediate_rate_first_order
           FROM first_date
           WHERE rank=1 
             """).show()