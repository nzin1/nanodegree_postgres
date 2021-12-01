# DROP TABLES

song_table_drop = "DROP TABLE IF EXISTS songs;"
artists_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"
users_table_drop = "DROP TABLE IF EXISTS users;"
songplays_table_drop = "DROP TABLE IF EXISTS songplays;"

# CREATE TABLES
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INTEGER,
    duration FLOAT
);""")

songplays_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT,
        location VARCHAR,
        user_agent VARCHAR   
);""")

artists_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR NOT NULL PRIMARY KEY,
    name VARCHAR,
    location VARCHAR,
    latitude FLOAT,
    longitude FLOAT
);""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP NOT NULL PRIMARY KEY,
    hour INTEGER, 
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday VARCHAR
);""")

users_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR, 
    level VARCHAR
);""")

# INSERT TABLES
song_table_insert = """INSERT INTO songs 
(song_id, title, artist_id, year, duration)  VALUES( %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; """

artists_table_insert = """INSERT INTO artists 
(artist_id, name, location, latitude, longitude)  VALUES( %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; """

time_table_insert = """INSERT INTO time 
(start_time, hour, day, week, month, year, weekday)  VALUES( %s, %s, %s, %s, %s, %s, %s) ON CONFLICT(start_time) DO NOTHING; """                 

users_table_insert = """INSERT INTO users 
(user_id, first_name, last_name, gender, level)  VALUES( %s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level; """                 

songplays_table_insert = """INSERT INTO songplays
(songplay_id, start_time, user_id, level, song_id,
                           artist_id, session_id, location, user_agent)
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s); """


# SELECT TABLES
song_select = """SELECT songs.song_id, artists.artist_id from songs
                     JOIN artists ON songs.artist_id =artists.artist_id
                    where songs.title = %s and artists.name = %s and songs.duration = %s """

# QUERY LISTS

create_table_queries = [song_table_create, artists_table_create, time_table_create,users_table_create, songplays_table_create]
drop_table_queries = [song_table_drop, artists_table_drop, time_table_drop, users_table_drop, songplays_table_drop]
insert_table_queries = [song_table_insert, artists_table_insert, time_table_insert,users_table_insert, songplays_table_insert]
select_table_queries = [song_select]