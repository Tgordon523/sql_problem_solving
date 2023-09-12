import duckdb

sql_init = """
CREATE table IF NOT EXISTS Tweets (tweet_id integer, content varchar);INSERT INTO Tweets values (1, 'Vote for Biden'); INSERT INTO Tweets values (2, 'Let us make America great again!');
"""

# print(duckdb.sql('SELECT 42').show())

r1 = duckdb.sql(sql_init)

duckdb.sql('SELECT tweet_id FROM Tweets WHERE LEN(content) < 15').show()
result = duckdb.sql('SELECT tweet_id FROM Tweets WHERE LEN(content) < 15').fetchall()
print(result)