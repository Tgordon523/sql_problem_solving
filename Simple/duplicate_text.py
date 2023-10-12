import duckdb

"""
Problem: 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
"""

sql_init = """
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
    DELETE 
    FROM Person p, Person e
    WHERE p.id > e.id AND p.email=e.email
""").show()