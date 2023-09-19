import duckdb

"""
Problem:

Find all numbers that appear atleast 3 times consecutively
"""

sql_init = """
Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           SELECT DISTINCT num
           FROM 
           (
           SELECT 
           LAG(num) OVER (ORDER BY id ASC) prev_num,
           LEAD(num) OVER (ORDER BY id ASC) new_num,
            * 
           FROM Logs
           ) fix
           WHERE 
           fix.num=fix.prev_num
           AND fix.num=fix.new_num

            """).show()