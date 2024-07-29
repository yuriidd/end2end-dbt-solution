pip install --upgrade pip
pip install psycopg2 

cd /app/

echo "Data migration: Creating database"
python 01-create-db.py
sleep 15
echo "Data migration: Creating tables"
python 02-create-tables.py
sleep 10
echo "Data migration: Loading data to database"
python 03-load-csv.py
echo "Data migration: Done"