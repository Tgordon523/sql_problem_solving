import duckdb

sql_init = """
CREATE TYPE action AS ENUM ('confirmed', 'timeout');
Create table If Not Exists Signups (user_id int, time_stamp datetime);
Create table If Not Exists Confirmations (user_id int, time_stamp datetime, action_state action);
Truncate table Signups;
insert into Signups values (3, '2020-03-21 10:16:13');
insert into Signups values (7, '2020-01-04 13:57:59');
insert into Signups values (2, '2020-07-29 23:09:44');
insert into Signups values (6, '2020-12-09 10:39:37');
Truncate table Confirmations;
insert into Confirmations values (3, '2021-01-06 03:30:46', 'timeout');
insert into Confirmations values (3, '2021-07-14 14:00:00', 'timeout');
insert into Confirmations values (7, '2021-06-12 11:57:29', 'confirmed');
insert into Confirmations values (7, '2021-06-13 12:58:28', 'confirmed');
insert into Confirmations values (7, '2021-06-14 13:59:27', 'confirmed');
insert into Confirmations values (2, '2021-01-22 00:00:00', 'confirmed');
insert into Confirmations values (2, '2021-02-28 23:59:59', 'timeout');
"""

# print(duckdb.sql('SELECT 42').show())

r1 = duckdb.sql(sql_init)

duckdb.sql("""SELECT S.user_id, COALESCE(c_rate.confirmation_rate, 0.0) confirmation_rates
           FROM Signups S 
           LEFT JOIN (
           SELECT
           C.user_id, SUM(CASE WHEN C.action_state = 'confirmed' THEN 1 ELSE 0 END) / COUNT(C.action_state) confirmation_rate
           FROM Confirmations C
           GROUP BY C.user_id
           ) c_rate ON S.user_id = c_rate.user_id

             """).show()
# result = duckdb.sql('SELECT tweet_id FROM Tweets WHERE LEN(content) < 15').fetchall()
# print(result)