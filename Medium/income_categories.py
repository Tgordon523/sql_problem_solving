import duckdb

"""
Problem:

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
"""

sql_init = """
Create table If Not Exists Accounts (account_id int, income int);
Truncate table Accounts;
insert into Accounts (account_id, income) values ('3', '108939');
insert into Accounts (account_id, income) values ('2', '12747');
insert into Accounts (account_id, income) values ('8', '87709');
insert into Accounts (account_id, income) values ('6', '91796');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           WITH salary AS (
           SELECT COALESCE(COUNT(account_id),0) accounts_cnt,
           (CASE WHEN income < 20000 THEN 'Low Salary'
           WHEN income > 20000 and income < 50000 THEN 'Average Salary'
           ELSE 'High Salary' END) bands
           FROM Accounts       
           GROUP BY bands
           )

           SELECT *
           FROM salary
            """).show()

