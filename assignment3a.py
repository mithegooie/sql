import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    nums = [(random.randint(0, 100),) for num in range(100)]

    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num INT)")

    c.executemany("INSERT INTO numbers VALUES(?)", nums)