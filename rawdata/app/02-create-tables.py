import psycopg2
import csv

# Enter you credentials
your_db = "host=YOUR_DATABASE_ADDRESS dbname=YOUR_NEW_DATABASE_NAME user=USERNAME password=PASSWORD"


### Connect to your database

conn = psycopg2.connect(your_db)
cursor = conn.cursor()
conn.autocommit = True

cursor.execute("DROP SCHEMA IF EXISTS raw;")
cursor.execute("CREATE SCHEMA raw;")

cursor.close()
conn.close()



### Create tables orders, managers, returns

conn = psycopg2.connect(your_db)
cursor = conn.cursor()
conn.autocommit = True

cursor.execute("DROP TABLE IF EXISTS raw.orders;")
cursor.execute("""
	CREATE TABLE raw.orders (
	row_id INT,
	order_id INT,
	order_date DATE,
	ship_date DATE,
	ship_mode VARCHAR(30),
	order_priority VARCHAR(30),
	product_container VARCHAR(30),
	customer_name VARCHAR(250),
	customer_segment VARCHAR(100),
	zip_code VARCHAR(10),
	state VARCHAR(50),
	city VARCHAR(50),
	region VARCHAR(50),
	product_category VARCHAR(250),
	product_subcategory VARCHAR(250),
	product_name VARCHAR(250),
	unit_price NUMERIC,
	quantity INT,
	sales NUMERIC,
	profit NUMERIC,
	discount NUMERIC,
	shipping_cost NUMERIC,
	product_base_margin NUMERIC,
	_etl_loadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
""")

cursor.execute("DROP TABLE IF EXISTS raw.managers;")
cursor.execute("""
	CREATE TABLE raw.managers (
	region VARCHAR(10),
	manager VARCHAR(30),
	_etl_loadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
""")

cursor.execute("DROP TABLE IF EXISTS raw.returns;")
cursor.execute("""
	CREATE TABLE raw.returns (
	order_id INT,
	status VARCHAR(10),
	_etl_loadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
""")

cursor.close()
conn.close()







