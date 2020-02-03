# CodeWars SQL
### SQL Basics: Simple WITH 
### Answered On: 02/02/2020

### INSTRUCTIONS:
### https://www.codewars.com/kata/5811501c2d35672d4f000146/train/sql


WITH

special_sales AS 
(
  SELECT 
    id,
    department_id,
    name,
    card_name,
    card_number,
    transaction_date
  FROM sales
  WHERE 
    price > 90
)

SELECT 
  id,
  name
FROM departments
WHERE 
  id IN (select department_id from special_sales);