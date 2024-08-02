
-- stg_superstore__managers

{{ config(
    materialized="table"
) }}

WITH managers AS (SELECT * FROM {{ source('superstore', 'managers') }})

SELECT
	region
	, manager
	, _etl_loadtime AS _etl_loadtime
	--
	, 'superstore' AS datasource
FROM managers

