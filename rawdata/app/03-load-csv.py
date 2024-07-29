import psycopg2
import csv

# Enter you credentials
your_db = "host=YOUR_DATABASE_ADDRESS dbname=YOUR_NEW_DATABASE_NAME user=USERNAME password=PASSWORD"


### Insert data 

conn = psycopg2.connect(your_db)
cursor = conn.cursor()
conn.autocommit = True

with open('Sample - Superstore Sales - Orders.csv', 'r') as f:
    cursor.copy_expert("""
	COPY raw.orders (
		row_id,
		order_id,
		order_date,
		ship_date,
		ship_mode,
		order_priority,
		product_container,
		customer_name,
		customer_segment,
		zip_code,
		state,
		city,
		region,
		product_category,
		product_subcategory,
		product_name,
		unit_price,
		quantity,
		sales,
		profit,
		discount,
		shipping_cost,
		product_base_margin) 
	FROM STDIN WITH CSV HEADER""", f)

with open('Sample - Superstore Sales - Returns.csv', 'r') as f:
    cursor.copy_expert("COPY raw.returns (order_id, status) FROM STDIN WITH CSV HEADER", f)

with open('Sample - Superstore Sales - Users.csv', 'r') as f:
    cursor.copy_expert("COPY raw.managers (region, manager) FROM STDIN WITH CSV HEADER", f)	

cursor.close()
conn.close()