import duckdb

"""
Problem:

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
"""

sql_init = """
Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null);
Truncate table RequestAccepted;
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           WITH userids AS (
           SELECT requester_id as ids FROM RequestAccepted

           UNION ALL

           SELECT accepter_id as ids FROM RequestAccepted
           ),
           totals AS 
           (
           SELECT ids, COUNT(*) cnt  
           FROM userids
           GROUP BY ids
           )



           SELECT ids, cnt
           FROM totals U
           WHERE U.cnt = (SELECT MAX(cnt) FROM totals)

            """).show()