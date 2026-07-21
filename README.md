# ETL Sales Analytics Project

## Overview

The ETL Sales Analytics Project is an end-to-end Data Analytics project that demonstrates the complete ETL (Extract, Transform, Load) process using Python, MySQL, SQL, and Power BI.

The project starts with a messy e-commerce sales dataset, performs data cleaning and transformation using Python, loads the cleaned data into MySQL, analyzes the data using SQL queries, and finally visualizes business insights through an interactive Power BI dashboard.


# Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- SQL
- SQLAlchemy
- PyMySQL
- Power BI
- Git
- GitHub

# Project Structure

ETL-Sales-Analytics-Project

── Images
── Dashboard Screenshot.png

── main.py
── messy_ecommerce_sales_data.csv
── cleaned_ecommerce_sales.csv
── analysis_queries.sql
── ETL Pipeline Dashboard.pbix
── ETL Pipeline_sql project.sql
── requirements.txt
── README.md

# ETL Pipeline

### Extract

- Imported raw e-commerce dataset
- Connected Python with MySQL

### Transform

- Removed duplicate records
- Handled missing values
- Converted data types
- Standardized categorical values
- Removed invalid records
- Feature Engineering
- Business Calculations

### Load

- Loaded cleaned dataset into MySQL
- Performed SQL Analysis
- Connected Power BI with cleaned dataset

# Dashboard KPIs

- 💰 Total Sales
- 📈 Total Profit
- 🧾 Average Sales
- 🎁 Total Discount
- 👥 Total Customers

# Dashboard Visualizations

- Monthly Sales Trend
- Category-wise Sales
- Top Products
- Payment Method Distribution
- Customer Segment Analysis
- Order Status Distribution
- Sales by Month

# Data Cleaning Steps

- Removed Duplicate Records
- Handled Missing Values
- Converted Date Format
- Converted Numeric Columns
- Standardized Categories
- Removed Invalid Quantity
- Removed Invalid Price
- Validated Total Amount
- Created New Features

# Feature Engineering

Created the following new columns:

- Year
- Month
- Month Number
- Day
- Day Name
- Quarter
- Weekend
- Order Size
- Price Category
- Customer Type
- Cost
- Profit
- Discount
- Final Amount

#  SQL Analysis

Performed SQL queries including:

- Total Sales
- Category-wise Sales
- Monthly Sales
- Top Products
- Customer Analysis
- Payment Analysis
- Order Status Analysis
- Aggregate Functions
- GROUP BY
- ORDER BY
- HAVING
- Window Functions

#  Power BI Dashboard

The dashboard contains:

- KPI Cards
- Interactive Filters
- Sales Trend
- Category Sales
- Top Products
- Customer Segment
- Payment Distribution
- Monthly Sales
- Order Status


#  Dashboard Preview

Dashboard Screenshot

"C:\Users\HP\OneDrive\Desktop\DSAAI\All projects in one file\ETL Pipeline project\ETL_PROJECT\Dashboard Screenshot.png"

# How to Run

### Clone Repository

git clone https://github.com/SonawaneRani/ETL-Sales-Analytics-Project.git


### Install Libraries

pip install -r requirements.txt

### Run Project

python main.py

Open the Power BI dashboard using:

ETL Pipeline Dashboard.pbix

# Future Improvements

- Automated ETL Pipeline
- Real-time Dashboard
- Cloud Deployment
- Streamlit Web Application
- Scheduled Data Refresh


# Author

**Rani Anand Sonawane**

B.Tech Computer Engineering (2025)

Aspiring Data Analyst

GitHub:
https://github.com/SonawaneRani
