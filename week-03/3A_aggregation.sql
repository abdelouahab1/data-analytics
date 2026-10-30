USE northwind;


-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC
LIMIT 1;

-- 2. Write a query to find the average price of all items that Northwind sells. (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.)

SELECT ROUND(AVG(UnitPrice), 2) as `average price`
FROM products;

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.

SELECT ProductName, UnitPrice, CompanyName
FROM products p
INNER JOIN suppliers s ON p.SupplierID = s.SupplierID 
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).

SELECT SUM(Salary)
FROM employees;

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(Salary) as `highest salary`, MIN(Salary) as `lowest salary`
FROM employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. Hint: Join is your friend here.

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID)
FROM suppliers s
INNER JOIN products p ON p.SupplierID = s.SupplierID 
GROUP BY s.SupplierID, s.CompanyName;

-- 7. Write a query to find the list of all category names and the average price for items in each category.

SELECT CategoryName , AVG(UnitPrice) as `Average Price`
FROM categories c
join products p ON c.CategoryID = p.CategoryID
GROUP BY CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.

SELECT  s.CompanyName, COUNT(p.ProductID)
FROM suppliers s
INNER JOIN products p ON p.SupplierID = s.SupplierID 
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) as `Inventory Value`
FROM products
ORDER BY `Inventory Value`;