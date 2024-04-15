#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table\
of hbtn_0e_0_usa where name matches the argument
"""

from sys import argv
import MySQLdb as db

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="UTF8")
    cur = db.cursor
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    results = cur.fetchall()
    for r in results:
        print(r)
    cur.close()
    db.close()
