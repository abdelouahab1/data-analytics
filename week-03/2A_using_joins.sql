USE northwind;

-- 1. Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.

SELECT ProductID, ProductName, UnitPrice, c.CategoryName
FROM products p
inner JOIN categories c
      ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, ProductName;

-- 2. Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.

SELECT ProductID, ProductName, UnitPrice, s.ContactName
FROM products p
inner JOIN suppliers s
      ON p.SupplierID = s.SupplierID
WHERE UnitPrice > 75;

-- 3. Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.

SELECT
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.ContactName AS SupplierName
FROM products p
INNER JOIN categories c
    ON p.CategoryID = c.CategoryID
INNER JOIN suppliers s
    ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

-- 4. Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.

SELECT
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    s.CompanyName AS Shipper
FROM orders o
INNER JOIN shippers s
    ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName;

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.

SELECT
    o.ShipName,
    COUNT(o.OrderID) AS OrderCount
FROM orders o
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName
ORDER BY o.ShipName;

-- 6. Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale

SELECT
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM orders o
JOIN `order details` od
    ON o.OrderID = od.OrderID
JOIN products p
    ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale'
ORDER BY o.OrderID;