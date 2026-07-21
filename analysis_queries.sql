USE ETL;

SELECT *
FROM cleaned_ecommerce_sales;

#Create SQL Views

#Total Sales
SELECT SUM(Total) AS Total_Sales
FROM cleaned_ecommerce_sales;

#Total Orders
SELECT COUNT(*) AS Total_Orders
FROM cleaned_ecommerce_sales; 

#Average Order Value
SELECT AVG(Total) AS Average_Order_Value
FROM cleaned_ecommerce_sales;

#Top selling products 
SELECT Product,
SUM(Total) AS Sales
FROM Cleaned_ecommerce_sales
GROUP BY Product
ORDER BY Sales DESC;

#Category Wise Sales
SELECT Category,
SUM(Total) AS Sales
FROM Cleaned_ecommerce_sales
GROUP BY Category
ORDER BY Sales DESC;

#Monthly Sales
SELECT Month,
SUM(Total) AS Sales
FROM cleaned_ecommerce_sales
GROUP BY Month
ORDER BY Sales DESC;

#Payment Method Analysis
SELECT Payment_Method,
COUNT(*) AS Orders
FROM cleaned_ecommerce_sales
GROUP BY Payment_Method;

#status Analysis
SELECT Status,
COUNT(*) AS Orders
FROM Cleaned_ecommerce_sales
GROUP BY Status;

#Customer Type
SELECT
Customer_Type,
COUNT(*) AS Customers
FROM Cleaned_ecommerce_sales
GROUP BY Customer_Type;

#Profit
SELECT SUM(Profit) AS Total_profit
FROM Cleaned_ecommerce_sales;

#Discount
SELECT
SUM(Discount) AS Total_Discount
FROM Cleaned_ecommerce_sales;

#Weekend vs Weekday
SELECT Weekend,
SUM(Total) AS Sales
FROM Cleaned_ecommerce_sales
GROUP BY Weekend;

# Price category
SELECT Price_category,
COUNT(*) AS Products
FROM Cleaned_ecommerce_sales
GROUP BY Price_category;

#order size
SELECT Order_size,
COUNT(*) AS Orders
FROM Cleaned_ecommerce_sales
GROUP BY Order_size;

# Highest Profit Product
SELECT Product,
SUM(Profit) AS Profit
FROM cleaned_ecommerce_sales
GROUP BY Product
ORDER BY Profit DESC
LIMIT 5;

#Highest Spending Customer
SELECT Customer_Name,
SUM(Total) AS Spending
FROM cleaned_ecommerce_sales
GROUP BY Customer_Name
ORDER BY Spending DESC
LIMIT 10;

#Top Months
SELECT Month,
SUM(Profit) AS Profit
FROM cleaned_ecommerce_sales
GROUP BY Month
ORDER BY Profit DESC;


#Category + Profit
SELECT
Category,
SUM(Profit) AS Profit
FROM cleaned_ecommerce_sales
GROUP BY Category
ORDER BY Profit DESC;

#Payment + Revenue
SELECT
Payment_Method,
SUM(Total) AS Revenue
FROM cleaned_ecommerce_sales
GROUP BY Payment_Method;

#Final Dashboard Query
SELECT
COUNT(*) Total_Orders,
SUM(Total) Total_Revenue,
SUM(Profit) Total_Profit,
AVG(Total) Average_Order_Value
FROM cleaned_ecommerce_sales;

# Stored Procedures

DELIMITER //

CREATE PROCEDURE GetTopProducts()
BEGIN

SELECT
Product,
SUM(Total) AS Sales
FROM cleaned_ecommerce_sales
GROUP BY Product
ORDER BY Sales DESC;

END //

DELIMITER ;
CALL GetTopProducts();

DELIMITER //

CREATE PROCEDURE GetCategorySales()
BEGIN

SELECT
Category,
SUM(Total) AS Sales
FROM cleaned_ecommerce_sales
GROUP BY Category;

END //

DELIMITER ;
CALL GetCategorySales();








