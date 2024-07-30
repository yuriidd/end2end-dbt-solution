# end-2-end-dbt-solution project

**That's async project "End to end Analytics solution with dbt and looker" from [Surfalytics](https://github.com/surfalytics/data-projects/tree/main/async-projects/01-end-to-end-analytics-with-dbt-and-looker).**

Prerequisites:

- git
- SQL, any database like Postgres
- simple python
- docker
- dbt

# Preface

What's the goal? Build end to end solution from describing your raw data to implementing data transformation chain across development to production environment using dbt Core as main Transformation tool.

Loading raw data to your DB/DWH doesn't play a big role as for me, I think its just necessary starting point, you can implement it different ways. Main course play around dbt transformations and its features.

![](_att/Pasted%20image%2020240725090345.png)

Picture above has a great view of range of tasks you can solve in one tool.


# Choosing DB/DWH

You have a wide choice. If you plan do everything local - you can choose PostgresSQL database. 

I prepared [docker image with Superstore sample csv's](https://github.com/yuriidd/dc-pg-superstore) with schema creating and autoload data at start. Variant with ready star schema also available.


# Project progress


## Week 1

**Git.** 

- Created new repository `dc-pg-superstore`
- Created this repository `end-2-end-dbt-solution`
- Updated `README` and `.gitignore`.

---

## Week 2

**Source data migration.** Goals:

1. Connect database
2. Ingest data from CSV's to database

I spend some time to create [Postgres with Superstore database in Docker](https://github.com/yuriidd/dc-pg-superstore/tree/main). I will use that Postgres with some modifications.

### Network

Main goals of modifications - to have access from Windows VSCodium (VSCode) to docker image through SSH with working dbt plagins for VSCodium. That's why I don't use Docker Desktop, but Docker Engine inside WSL instead. dbt Core doesn't provide column lineage, but you can obtain it by plugins from IDE. They are very usefull for dbt development. ***If you have MacBook either not interested in dbt plugins just skip any network options.***

**Network explain [here](w2network.md).**

Create Network (or skip):

```shell
docker network create -d ipvlan \
	--attachable \
	--subnet=172.23.160.0/20	\
	--gateway=172.23.160.1 \
	-o ipvlan_mode=l2 \
	-o parent=eth0 \
	dbt-net
```

### Local Postgres + data loading

Clone [repository](https://github.com/yuriidd/dc-pg-superstore/tree/main), (optional) add network parameters, run docker:

```shell
cd ~
git clone git@github.com:yuriidd/dc-pg-superstore.git

cd dc-pg-superstore

docker container run -it -d --name pg16-superstor \
    -e POSTGRES_USER=pguser1 \
    -e POSTGRES_PASSWORD=pgpass123 \
    -e POSTGRES_DB=superstore_db \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -p 5432:5432 \
    -v "$(pwd)"/pg-init.d:/docker-entrypoint-initdb.d \
    -v "$(pwd)"/data:/var/lib/postgresql/data \
    -v "$(pwd)"/csv:/csv \
    --network=dbt-net \
 	--ip=172.23.174.10 \
    postgres:16
```

### Manual data loading

There are [three methods of loading CSV's](rawdata/load2db.md) to remote database:

- From docker container
- With local python environment
- From you IDE

### Summary

- Source files and Database found
- Data was loaded
- Custom network created
- Updated `README`, network and data load instructions

---

## Week 3

**dbt Core.** Goals:

- Setup dbt Core.
- Define `sources`, `profiles`
- Define `dev` and `prod` schemas and targets
- Create staging models

In progress . . .

