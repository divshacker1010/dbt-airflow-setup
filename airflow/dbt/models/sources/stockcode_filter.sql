{{ config(materialized='table') }}

SELECT
  *
FROM retail_info_table
where stockcode = '85231B'
