import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    sql = {"AVG": "SELECT AVG(num) from numbers",
           "MAX": "SELECT MAX(num) from numbers",
           "MIN": "SELECT MIN(num) from numbers",
           "SUM": "SELECT SUM(num) from numbers"
        }

    while True:
        user_choice = raw_input("Enter 'AVG', 'MAX', 'MIN', 'SUM' or 'exit':")
        try:
            c.execute(sql[user_choice.upper()])
            result = c.fetchone()
            print "{}: {}".format(user_choice.upper(), result[0])
        except:
            print "Goodbye"
            exit()