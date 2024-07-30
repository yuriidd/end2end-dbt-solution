> [Start](../README.md) >> Loading CSVs to Postgres database

# Loading CSVs to Postgres database

There are sample data and scripts for data migration.

```shell
end2end-dbt-solution
└── rawdata
	└── app
	    ├── 01-create-db.py
	    ├── 02-create-tables.py
	    ├── 03-load-csv.py
	    ├── Sample - Superstore Sales - Orders.csv
	    ├── Sample - Superstore Sales - Returns.csv
	    ├── Sample - Superstore Sales - Users.csv
	    └── init-load2db.sh
```

You have a few choices how to insert your data to your database:


##  1. From docker container

- Modify python-scripts `01-create-db.py`, `02-create-tables.py`, `03-load-csv.py` according to your database in `app` directory. 
- Go to `rawdata` directory: 

```
cd ~/end2end-dbt-solution/rawdata
```

- Run docker command:

```shell
docker run --rm -it -d --name load2db \
    -v $(pwd)/app:/app \
    python:3.10 /bin/bash -c "/app/init-load2db.sh"
```

That's my preferred choice because python inside container does not need additional steps for creating environment + auto remove.

Either you can run docker container, go to `/app` and run init script or python scripts separately even in python shell:

```shell
docker run -it --name load2db \
    -v $(pwd)/app:/app \
    python:3.10 /bin/bash
```


##  2. With local python environment

- Modify python-scripts according to your database. 

- Create python `venv` at your directory.
- Install your python-scripts dependencies.

- Run python-scripts consistently or run `init-load2db.sh` from `end2end-dbt-solution/rawdata/app` directory.

```shell
cd ~/end2end-dbt-solution/rawdata/app

python3 -m venv venv
source venv/bin/activate

pip install psycopg2

init-load2db.sh
```


## 3. From you IDE

DBeaver or other IDE give you some way to ingest CSV's to Database.

---

> [Start](../README.md) >> Loading CSVs to Postgres database

