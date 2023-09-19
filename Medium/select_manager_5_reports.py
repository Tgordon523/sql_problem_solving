import duckdb

"""
Problem:

Return managers with 5 or more direct reports
"""

sql_init = """
Create table If Not Exists Employee (id int, name varchar, department varchar, managerId int);
Truncate table Employee;
insert into Employee (id, name, department, managerId) values (101, 'John', 'A', 0);
insert into Employee (id, name, department, managerId) values (102, 'Dan', 'A', 101);
insert into Employee (id, name, department, managerId) values (103, 'James', 'A', 101);
insert into Employee (id, name, department, managerId) values (104, 'Amy', 'A', 101);
insert into Employee (id, name, department, managerId) values (105, 'Anne', 'A', 101);
insert into Employee (id, name, department, managerId) values (106, 'Ron', 'B', 101);
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""SELECT E.name
           FROM Employee E
           JOIN (
           SELECT managerId, COUNT(*) total
           FROM Employee
           GROUP BY managerId
           HAVING COUNT(*) >= 5
           ) reports ON E.id=reports.managerId
             """).show()