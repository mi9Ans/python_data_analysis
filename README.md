## 🛍️ Project #25: Product Sales Analysis

Analyze basic sales data from a CSV file using Python and **Pandas**.

---

### 📂 Files in This Project

- `product_sales.csv` — Sample product sales data
- `product_sales_analysis.py` — Python script to process and summarize the data

---

### ▶️ How to Run

1. Make sure `pandas` is installed:
```bash
pip install pandas
2. Run the script
python product_sales_analysis.py

📊 Product Sales Summary
----------------------------
    Product  Units_Sold  Unit_Price  Revenue
0  Notebook          120        2.50    300.00
1       Pen          250        1.20    300.00
2    Eraser          180        0.50     90.00
3    Marker          100        1.75    175.00
4     Scale           75        1.50    112.50

💰 Total Revenue: $977.50
🏆 Best Seller: Pen
📈 Average Units Sold: 145.00

👨‍💻 Author
Anshumaan Mishra


### 📊 Project 25 – Performance Analysis by Class & Gender

### 🧠 Objective
This project analyzes student performance in **Math** and **English** based on their **Class** and **Gender**, using the `pandas` library.

---

### 📁 Files Included
- `performance_analysis.py` – Main script
- `student_extended.csv` – Input CSV dataset
- `sample_output.png` – Screenshot of output

---

### 🛠️ Features
- Grouped analysis using `.groupby()` on `Class` and `Gender`
- Calculates:
  - 📉 Minimum
  - 📈 Maximum
  - 🧮 Average
  - 🔢 Count
- Outputs clearly structured data tables for easy comparison

---

### 📥 Sample Input (CSV)

```csv
Name,Class,Gender,Math,English
Amit,10,M,85,81
Neha,10,F,92,95
Ravi,11,M,78,76
Simran,11,F,90,85
Arjun,10,M,65,89
Sana,11,F,71,70
Karan,11,M,84,80
Divya,11,F,72,78
....
````
🖨️Sample Output(Text Perview)

### 🖨️ Sample Output

![sample output](sample_output.png)

Group-wise Average(Class & Gender)
                    Math  English
Class Gender                    
10    F              92      95
      M              75      85
11    F              77.7    77.6
      M              81      78

Aggregated Scores (min, max, count)
                   Math                English           
                   min  max count     min  max count
Class Gender                                        
10    F             92   92     1      95   95     1
      M             65   85     2      81   89     2
11    F             71   90     3      70   85     3
      M             78   84     2      76   80     2

▶️How to Run 

Make sure pandas is installed. Then run the script using:

python performance_analysis.py

🧑‍💻 Author & Info
Author: Anshumaan Mishra

Date: July 2025

Category: Beginner Pandas Project

## 📊 Project 26 – Product Sales Summary

### 🧠 Objective
Analyze a CSV file containing product sales and extract key insights like total sales, top performer, and average performance using **pandas**.

---

### 📁 Files Included
- `product_sales_analysis.py` – Main script for analysis
- `product_info.csv` – Sample input data

---

### 🛠️ Features
- ✅ Reads CSV using `pandas`
- 📈 Calculates:
  - Total Units Sold
  - Top-Selling Product
  - Average Units Sold
- 🔽 Sorts products by units sold in descending order

---

### 📥 Sample Input (CSV)

```csv
Product,Units Sold
Laptop,150
Phone,200
Tablet,120
Monitor,180
Keyboard,90

   Product  Units Sold
0   Laptop          150
1    Phone          200
2   Tablet          120
3  Monitor          180
4 Keyboard           90

Total Units Sold: 740

Top-Selling Product:
  Product  Units Sold
1   Phone         200

Average Units Sold: 148.0

Sorted Products by Sales:
  Product  Units Sold
1   Phone         200
3  Monitor        180
0   Laptop        150
2   Tablet        120
4 Keyboard         90

➡️How to run
Make sure pandas is installed:
pip install pandas

Then run:
python product_sales_analysis.py

👨‍💻 Author
Anshumaan Mishra


## 🧹 Student Survey Data Cleaning

This project focuses on cleaning a student survey dataset using Python and `pandas`.  
It handles missing values, inconsistent formats, and duplicates to prepare the data for analysis.

---

### ✅ Features

- Drops rows that are completely empty
- Fills missing age values with the rounded mean
- Converts age column to nullable `Int64`
- Standardizes gender entries (like 'm', 'M', 'male') → `Male`
- Title-cases and strips whitespace from names
- Removes duplicate entries
- Displays:
  - Gender counts
  - Number of unique cities

---

### 📊 Sample Output

Gender
Male 4
Female 3
Name: Gender, dtype: int64
Unique Cities: 9
Name Age Gender City
0 Alice 25 Female Delhi
1 Bob 30 Male delhi
...


---

### 🛠 Technologies Used

- Python 3.x 🐍
- pandas

---

### 🚀 How to Run

Make sure all files are in the same folder.

```bash
python student_data.py

👨‍💻 Author
Anshumaan Mishra


