#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name like 'N%' ORDER BY stetes.id ASC" 
    cursor.excute(query)
    states  = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
