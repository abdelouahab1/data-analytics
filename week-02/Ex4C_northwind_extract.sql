USE northwind; 
 
-- 4. The products table holds the items Northwind sells. 
-- The categories table holds the types/categories of products Northwind sells. 
 
 
-- 5. Retrieve all columns from the employees table. 
SELECT * 
FROM employees; 
 
-- The employee whose last name makes it look like she is a bird is Margaret Peacock. 
 
 
-- 6. Retrieve all columns from the products table. 
SELECT * 
FROM products; 
 
-- The standard Northwind database contains 77 product records. 
-- To retrieve only 10 rows using the toolbar, set the result limit to 10. 
-- BONUS: Use LIMIT 10 at the end of the query to return at most 10 rows. 
-- Source: MySQL Reference Manual, SELECT statement: 
-- https://dev.mysql.com/doc/refman/8.4/en/select.html 
 
 
-- 7. Retrieve all columns from the categories table. 
SELECT * 
FROM categories; 
 
-- The category ID for Seafood is 8. 
 
 
-- 8. Retrieve the first 50 orders with the requested columns. 
SELECT OrderID, OrderDate, ShipName, ShipCountry 
FROM orders 
LIMIT 50; 