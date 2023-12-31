import duckdb

"""
Problem:

Find all employees with no bonus or bonus under 1k
"""

sql_init = """
Create table If Not Exists Employee (empId int, name varchar, supervisor int, salary int); 
Create table If Not Exists Bonus (empId int, bonus int);
insert into Employee values (3, 'Brad', 0, '4000');
insert into Employee values (1, 'John', 3, '1000');
insert into Employee values (2, 'Dan', 3, '2000');
insert into Employee values (4, 'Thomas', 3, '4000');
insert into Bonus values (2, '500');
insert into Bonus values (4, '2000');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""SELECT * 
           FROM Employee E
           LEFT JOIN Bonus B ON E.empId=B.empId
           WHERE (B.bonus < 1000 OR B.bonus is NULL)  """).show()