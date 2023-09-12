import duckdb
import pandas as pd

sql_init = """
CREATE TYPE state AS ENUM ('approved', 'declined');
Create table If Not Exists Transactions (id int, country varchar,state state, amount int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values (121, 'US', 'approved', 1000, '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values (122, 'US', 'declined', 2000, '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values (123, 'US', 'approved', 2000, '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values (124, 'DE', 'approved', 2000, '2019-01-07');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""SELECT CONCAT(YEAR(trans_date), '-', MONTH(trans_date)) monthly, country, COUNT(*) trans_cnt, SUM(CASE WHEN T.state = 'approved' THEN 1 ELSE 0 END) approved_cnt, SUM(T.amount) total,
           SUM(CASE WHEN T.state = 'approved' THEN T.amount ELSE 0 END) approved_total
           FROM Transactions T
           GROUP BY 
           CONCAT(YEAR(trans_date), '-', MONTH(trans_date)), country
             """).show()

results = duckdb.sql("""SELECT CONCAT(YEAR(trans_date), '-', MONTH(trans_date)) monthly, country, COUNT(*) trans_cnt, SUM(CASE WHEN T.state = 'approved' THEN 1 ELSE 0 END) approved_cnt, SUM(T.amount) total,
           SUM(CASE WHEN T.state = 'approved' THEN T.amount ELSE 0 END) approved_total
           FROM Transactions T
           GROUP BY 
           CONCAT(YEAR(trans_date), '-', MONTH(trans_date)), country
             """).to_df()
print(results)