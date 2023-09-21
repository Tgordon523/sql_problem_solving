import duckdb

"""
Problem:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
"""

sql_init = """
Create table If Not Exists Movies (movie_id int, title varchar(30));
Create table If Not Exists Users (user_id int, name varchar(30));
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);
Truncate table Movies;
insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');
Truncate table Users;
insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'Ames');
Truncate table MovieRating;
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');
"""

r1 = duckdb.sql(sql_init)

duckdb.sql("""
           WITH rating as   (
           SELECT movie_id, AVG(rating) avg
           FROM MovieRating
           WHERE MONTH(created_at) = 2
           GROUP BY movie_id
           )
           
           SELECT M.title, R.avg
           FROM rating R
           JOIN Movies M ON R.movie_id = M.movie_id
           ORDER BY avg DESC, M.title
           LIMIT 1
           """).show()

duckdb.sql("""
           SELECT
           U.name, nums
           FROM Users U
           JOIN (
           SELECT user_id, COUNT(*) nums FROM MovieRating 
           GROUP BY user_id
           ) R on U.user_id=R.user_id
           ORDER BY nums DESC, U.name
           LIMIT 1
           
           

            """).show()