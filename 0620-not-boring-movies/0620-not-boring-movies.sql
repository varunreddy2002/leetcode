SELECT *
FROM Cinema
WHERE MOD(id, 2) != 0 AND description NOT LIKE '%boring%'
order by rating desc;
