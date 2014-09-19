# JOINing data from multiple tables


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT p.city, p.population, r.region
              FROM population p, regions r
              WHERE p.city = r.city
              ORDER BY p.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print