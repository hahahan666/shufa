cur.execute(
        "INSERT INTO works(name, homework, score, times) VALUES (%s, %s, 90,\
        (SELECT * FROM (SELECT count(*) + 1 FROM works WHERE name = %s) AS t));"\
        , (username, filename, username))