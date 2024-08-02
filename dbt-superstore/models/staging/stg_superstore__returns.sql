
-- stg_superstore__returns

{{ config(
    materialized="table"
) }}

WITH returns AS (SELECT * FROM {{ source('superstore', 'returns') }})

SELECT
	order_id
	, status
	, _etl_loadtime AS _etl_loadtime
	--
	, 'superstore' AS datasource
FROM returns