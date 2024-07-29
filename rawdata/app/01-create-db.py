import psycopg2
import csv

# Enter you credentials
standart_db = "host=YOUR_DATABASE_ADDRESS dbname=postgres user=pguser1 password=pgpass123"


### Create new database and schema

conn = psycopg2.connect(standart_db)
cursor = conn.cursor()
conn.autocommit = True

cursor.execute("DROP DATABASE IF EXISTS SURFALYTICS_DW_YURIIDD;")
cursor.execute("CREATE DATABASE SURFALYTICS_DW_YURIIDD;")

cursor.close()
conn.close()

