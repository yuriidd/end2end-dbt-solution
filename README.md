# end-2-end-dbt-solution project

**That's async project "End to end Analytics solution with dbt and looker" from [Surfalytics](https://github.com/surfalytics/data-projects/tree/main/async-projects/01-end-to-end-analytics-with-dbt-and-looker).**

# Preface

What's the goal? Build end to end solution from describing your raw data to implementing data transformation chain across development to production environment using dbt Core as main ETL tool.

Loading raw data to your DB/DWH doesn't play a big role as for me, I think its just necessary starting point, you can implement it different ways. Main course play around dbt transformations and its features.

![](_att/Pasted%20image%2020240725090345.png)

Picture above has a great view of range of tasks you can solve in one tool.

# Choosing DB/DWH

You have a wide choice. If you plan do everything local - you can choose PostgresSQL database. 

I prepared [docker image with Superstore sample csv's](https://github.com/yuriidd/dc-pg-superstore) with schema creating and autoload data at start. Variant with ready star schema also available.

# Project progress

## Week 1

**Git.** 

- Created repository for `dc-pg-superstore` and for current project.
- 



