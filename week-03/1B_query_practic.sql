USE northwind;

-- 1) Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- 2) Write a query to identify the products where the unit price is $7.50 or less.

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.50;

-- 3) What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?

SELECT ProductName
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;

-- 4) Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry

SELECT *
FROM products; -- it define the categories as CategoryID

SELECT *
FROM categories; -- the seafood categorie has the CategoryID = 8

SELECT ProductName
FROM products
WHERE CategoryID = 8;

-- 5) Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.

SELECT *
FROM products; -- we know the suppliers from the SupplierID

SELECT *
FROM suppliers; -- the supplier "Tokyo Trader" has the SupplierID number 4

SELECT ProductName
FROM products
WHERE SupplierID = 4;

-- 6) How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question.

SELECT COUNT(EmployeeID)
FROM employees; 

SELECT LastName
FROM employees
WHERE Title LIKE '%Manager%';

