#!/usr/bin/env python3
# import csv
import mysql.connector


db_conn = mysql.connector.connect(user='jop_etl_user', password='bobross',
                                  host='localhost', port=3306,
                                  db='joy_of_painting')
cursor = db_conn.cursor()
query = ("SHOW TABLES")

cursor.execute(query)

print(cursor.fetchall())

cursor.close()
db_conn.close()
