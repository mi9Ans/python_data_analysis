# 📊 Python Data Analysis Projects  

Beginner-friendly Python projects for analyzing real-world **CSV datasets** using **Pandas**.  
Covers **data cleaning, transformation, grouping, and summary reporting**.  

---

## 🛠️ Tech Stack  
- Python 🐍  
- Pandas 📊  

---

## 📂 Projects Included  

### 🧹 Project 1: Student Survey Cleaning  
**Objective:** Clean a messy student survey dataset with missing values and inconsistent casing.  

**Files:**  
- `student_survey_dirty.csv` → Raw input dataset (11 rows, messy formatting)  
- `student_data.py` → Cleaning script  

**Features:**  
- Handles missing values (`fillna`, `dropna`)  
- Normalizes text (title case for names/cities)  
- Converts `Age` column to integers  
- Checks unique values with `.nunique()` and `.value_counts()`  

---

### 🎓 Project 2: Student Performance Analysis  
**Objective:** Analyze student scores across subjects, cities, and gender.  

**Files:**  
- `student_performance.py` → Analysis script  
- `student_extended.csv` → Cleaned dataset (output)  

**Features:**  
- String cleaning (`strip`, `title`)  
- Gender normalization (`M` → Male, `F/f` → Female)  
- Score conversion to numeric with error handling  
- Drops duplicates  
- Calculates:  
  - Average scores  
  - Most common city  
  - Unique subjects/students  
  - Top scorer in Science  

---

### 🧠 Project 3: Student Performance by Class & Gender  
**Objective:** Group analysis of Math & English scores.  

**Files:**  
- `performance_analysis.py` → Grouped analysis script  
- `student_extended.csv` → Input dataset  
- `sample_output.png` → Example results  

**Features:**  
- `.groupby()` by Class & Gender  
- Aggregations: min, max, mean, count  
- Outputs structured comparison tables  

---

### 🛒 Project 4: Product Sales Analysis  
**Objective:** Process raw sales data and calculate revenue insights.  

**Files:**  
- `product_sales.csv` → Sample sales dataset  
- `product_sales_analysis.py` → Script for analysis  

**Features:**  
- Computes **Revenue = Units × Price**  
- Summarizes sales per product  
- Finds:  
  - 💰 Total Revenue  
  - 🏆 Best Seller  
  - 📈 Average Units Sold  

---

### 📦 Project 5: Product Sales Summary  
**Objective:** Summarize product sales performance.  

**Files:**  
- `product_info.csv` → Input dataset  
- `sales_summary_generator.py` → Script for summary  
- `sample_sales_generator.png` → Example output  

**Features:**  
- Reads sales data with pandas  
- Calculates:  
  - Total Units Sold  
  - Top-Selling Product  
  - Average Units Sold  
- Sorts results in descending order  

---

### 📑 Project 6: Sales Data Analysis  
**Objective:** Analyze transactional sales records.  

**Files:**  
- `sales_data.csv` → Raw dataset  
- `sales_analysis.py` → Script for processing  

**Features:**  
- Cleans and loads sales records  
- Performs grouping & summarization  
- Prepares data for reporting/dashboard  

---

## 🚀 How to Run  

1. Install requirements:
   ```bash
pip install pandas
3. Run any project script
   Example
   python student_performance.py

👨‍💻 Author  
Anshumaan Mishra  
Data Analyst (Python | Pandas | Data Cleaning | Reporting)
