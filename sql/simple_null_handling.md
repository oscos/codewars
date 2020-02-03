# CodeWars SQL
### simle_null_handling.md 
### Answered On: 02/01/2020

### INSTRUCTIONS:
### https://www.codewars.com/kata/5811315e04adbbdb5000050e/train/sql

```
SELECT 
  id,
  COALESCE(NULLIF(name,''),'[product name not found]') as name,
  NULLIF(price,0) as price,
  COALESCE(NULLIF(card_name,''),'[card name not found]') as card_name,
  card_number,
  transaction_date
FROM eusales
WHERE 
  price > 50
```