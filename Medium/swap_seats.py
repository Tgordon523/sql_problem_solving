import duckdb

"""
Problem:

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
"""

sql_init = """
Create table If Not Exists Seat (id int, student varchar(255));
Truncate table Seat;
insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           SELECT
           (CASE WHEN id % 2 THEN ifnull(lead(student) over (order by id),student)  
           ELSE LAG(student) OVER (ORDER BY id) END) new_order, 
           *
           FROM Seat

            """).show()