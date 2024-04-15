#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT cities.id FROM cities JOIN states ON
              cities.state_id = states.id WHERE states.name LIKE %s
              ORDER BY cities.id ASC", (argv[4],))
    results = c.fetchall()
    print(", ".join(city[0] for city in results))
