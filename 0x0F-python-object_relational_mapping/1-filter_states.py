#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)\
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="UTF8")
    # reate a cursor object to point through the rows
    cursor = db.cursor()

    # ecute the sql query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
