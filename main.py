from urllib.parse import quote_plus
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

username = "root"
password = quote_plus("Rani@2001")
host = "localhost"
port = "3306"
database = "ETL"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

query = "SELECT * FROM messy_ecommerce_sales_data"

df = pd.read_sql(query, engine)

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(df.head())
print(df.shape)
df.info()
print(df.describe(include='all'))
print("Invalid Quantity Rows")
print(df[df["Quantity"] <= 0])
df = df[df["Quantity"] > 0]

print(df.duplicated().sum())
print(df.columns)
print(df.dtypes)
print(df.nunique())

df.drop_duplicates(inplace=True)
df = df.replace(r'^\s*$', np.nan, regex=True)
print(df.isnull().sum())
print(df[df["Order_Date"].isnull()])
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

df["Order_Date"] = df["Order_Date"].fillna(
    df["Order_Date"].mode()[0]
)
df["Price"] = pd.to_numeric(df["Price"],errors="coerce")
df["Total"] = pd.to_numeric(df["Total"],errors="coerce")
print(df["Price"].isnull().sum())
print(df.dtypes)
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Total"] = df["Total"].fillna(df["Total"].median())
print(df["Total"].isnull().sum())
df["Product"] = df["Product"].fillna(df["Product"].mode()[0])
df["Category"] = df["Category"].fillna(df["Category"].mode()[0])
df["Payment_Method"] = df["Payment_Method"].fillna(df["Payment_Method"].mode()[0])
df["Status"] = df["Status"].fillna(df["Status"].mode()[0])
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
print("="*50)
print("Missing Values After Cleaning")
print("="*50)
print(df.isnull().sum())
print("="*50)
print("Data Types After Cleaning")
print("="*50)
print(df.dtypes)
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])
print("\nColumn Names")
for col in df.columns:
    print(col)
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Product")
plt.title("Product Distribution")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Category")
plt.title("Category Distribution")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Payment_Method")
plt.title("Payment Method Distribution")
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Status")
plt.title("Order Status")
plt.show()
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=15)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(8,5))
plt.hist(df["Total"], bins=15)
plt.title("Total Sales Distribution")
plt.xlabel("Total")
plt.ylabel("Frequency")
plt.show()
top_products = (
    df.groupby("Product")["Total"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

plt.figure(figsize=(10,5))

top_products.plot(kind="bar")

plt.title("Top 10 Products")

plt.ylabel("Sales")

plt.show()

top_category = (
    df.groupby("Category")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(top_category)

plt.figure(figsize=(8,5))

top_category.plot(kind="bar")

plt.title("Category Wise Sales")

plt.ylabel("Sales")

plt.show()

plt.figure(figsize=(6,5))

sns.heatmap(
    df[["Quantity","Price","Total"]].corr(),
    annot=True,
    cmap="coolwarm"
)

df["Category"] = df["Category"].replace("nan", np.nan)

df["Category"] = df["Category"].fillna("Unknown")

plt.title("Correlation Heatmap")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Total"])
plt.title("Outlier Detection")
plt.show()

df["Month"] = df["Order_Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Total"].sum()
print(monthly_sales)
plt.figure(figsize=(10,5))
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.ylabel("Sales")
plt.show()

print("="*60)
print("FEATURE ENGINEERING")
print("="*60)

df["Year"] = df["Order_Date"].dt.year
df["Month_No"] = df["Order_Date"].dt.month
df["Day"] = df["Order_Date"].dt.day
df["Day_Name"] = df["Order_Date"].dt.day_name()
df["Quarter"] = df["Order_Date"].dt.quarter

print(df[["Order_Date","Year","Month_No","Day","Day_Name","Quarter"]].head())

print("="*60)
print("WEEKEND FEATURE")
print("="*60)

df["Weekend"] = df["Day_Name"].isin(["Saturday", "Sunday"])

print(df[["Order_Date", "Day_Name", "Weekend"]].head(10))

print("="*60)
print("TOTAL VALIDATION")
print("="*60)

df["Expected_Total"] = df["Quantity"] * df["Price"]

print(df[["Quantity", "Price", "Total", "Expected_Total"]].head())

df["Difference"] = df["Expected_Total"] - df["Total"]

print(df[["Total", "Expected_Total", "Difference"]].head())

df["Total"] = df["Expected_Total"]
print(df[["Quantity", "Price", "Total"]].head())

wrong_records = df[df["Difference"] != 0]

print("="*60)
print("WRONG TOTAL RECORDS")
print("="*60)

print(wrong_records)

print("="*60)
print("STANDARDIZING CATEGORY NAMES")
print("="*60)

df["Category"] = df["Category"].str.strip()

df["Category"] = df["Category"].replace({
    "electronics":"Electronics",
    "ELECTRONICS":"Electronics",
    "electronic":"Electronics",
    "sports":"Sports",
    "books":"Books",
    "home":"Home",
    "clothing":"Clothing"
})

print(df["Category"].value_counts())

print("="*60)
print("STANDARDIZING STATUS")
print("="*60)

df["Status"] = df["Status"].str.strip().str.title()

print(df["Status"].value_counts())

print("="*60)
print("STANDARDIZING PAYMENT METHOD")
print("="*60)

df["Payment_Method"] = df["Payment_Method"].str.strip().str.title()

print(df["Payment_Method"].value_counts())

print("="*60)
print("REMOVING INVALID QUANTITY")
print("="*60)

df = df[df["Quantity"] > 0]

print(df.shape)

df = df[df["Price"] > 0]
print(df.shape)
df = df[df["Total"] > 0]

print(df.shape)

print("="*60)
print("FINAL DATA QUALITY CHECK")
print("="*60)

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.shape)

print("="*60)
print("FINAL CLEAN DATASET")
print("="*60)

print(df.head())
print(df.info())


print("="*60)
print("EXPECTED TOTAL CALCULATION")
print("="*60)

df["Expected_Total"] = df["Quantity"] * df["Price"]

print(df[["Quantity","Price","Total","Expected_Total"]].head(10))

print("="*60)
print("TOTAL VALIDATION")
print("="*60)

df["Difference"] = abs(df["Expected_Total"] - df["Total"])

wrong_records = df[df["Difference"] > 1]

print(wrong_records[[
    "Order_ID",
    "Quantity",
    "Price",
    "Total",
    "Expected_Total",
    "Difference"
]])

print("Incorrect Records :", len(wrong_records))

print("="*60)
print("CORRECTING TOTAL")
print("="*60)

df["Total"] = df["Expected_Total"]

print(df[["Quantity","Price","Total"]].head())

print("="*60)
print("ORDER SIZE")
print("="*60)

df["Order_Size"] = np.where(
    df["Quantity"] >= 4,
    "Large",
    "Small"
)

print(df["Order_Size"].value_counts())

print("="*60)
print("PRICE CATEGORY")
print("="*60)

df["Price_Category"] = pd.cut(
    df["Price"],
    bins=[0,200,500,1000],
    labels=["Low","Medium","High"]
)

print(df["Price_Category"].value_counts())

print("="*60)
print("CUSTOMER SEGMENT")
print("="*60)

customer_sales = (
    df.groupby("Customer_Name")["Total"]
      .transform("sum")
)

df["Customer_Type"] = np.where(
    customer_sales > 1000,
    "Premium",
    "Regular"
)

print(df["Customer_Type"].value_counts())

print("="*60)
print("PROFIT CALCULATION")
print("="*60)

df["Cost"] = df["Total"] * 0.70

df["Profit"] = df["Total"] - df["Cost"]

print(df[["Total","Cost","Profit"]].head())

print("="*60)
print("DISCOUNT")
print("="*60)

df["Discount"] = np.where(
    df["Total"] > 1000,
    df["Total"] * 0.10,
    0
)

print(df[["Total","Discount"]].head())

print("="*60)
print("FINAL AMOUNT")
print("="*60)

df["Final_Amount"] = (
    df["Total"] - df["Discount"]
)

print(df[["Total","Discount","Final_Amount"]].head())

print("="*60)
print("TRANSFORMED DATASET")
print("="*60)

print(df.head())

print(df.columns)

print(df.shape)

print(df.info())

print("="*60)
print("LOADING CLEAN DATA TO MYSQL")
print("="*60)

df.to_sql(
    name="cleaned_ecommerce_sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Successfully Loaded into MySQL")


print("="*60)
print("EXPORTING CLEAN DATASET")
print("="*60)

df.to_csv(
    "cleaned_ecommerce_sales.csv",
    index=False
)

print("CSV Saved Successfully")