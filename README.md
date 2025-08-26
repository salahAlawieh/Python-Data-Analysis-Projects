# Python Data Analysis Projects

This repository contains five projects completed as part of the **freeCodeCamp Data Analysis with Python** certification.  
Each project demonstrates practical skills in **Python, Pandas, NumPy, Matplotlib, and Seaborn** for data analysis, visualization, and basic predictions.

---

## 1. Projects Overview

### 1.1 [Demographic Data Analyzer](Project1_Demographic_Data_Analyzer)
- **Objective:** Analyze demographic data from the 1994 Census database using Pandas.  
- **Dataset:** Demographic data including age, workclass, education, marital status, occupation, race, sex, hours worked, and salary.  
- **Key Tasks:**
  - Count people by race and calculate average age of men.  
  - Compute percentages of people with Bachelor's and advanced education earning >50K.  
  - Analyze work hours, country-level income, and occupation trends.  
- **Skills Demonstrated:** Data cleaning, aggregation, groupby, filtering, and basic statistics.

### 1.2 [Mean-Variance-StandardDeviation Calculator](Project2_Mean_Var_Std_Calculator)
- **Objective:** Create a function to calculate mean, variance, standard deviation, max, min, and sum for a 3×3 matrix.  
- **Key Tasks:**
  - Convert a list of 9 numbers into a 3×3 NumPy array.  
  - Calculate metrics along rows, columns, and flattened matrix.  
  - Return results in a structured dictionary and handle invalid input.  
- **Skills Demonstrated:** Numerical computations with NumPy, array manipulation, and Python function design.

### 1.3 [Medical Data Visualizer](Project3_Medical_Data_Visualizer)
- **Objective:** Visualize medical examination data to explore cardiovascular risk factors.  
- **Dataset:** Patient data including age, height, weight, blood pressure, cholesterol, glucose, lifestyle habits, and cardio status.  
- **Key Tasks:**
  - Add an overweight column based on BMI.  
  - Normalize categorical variables (cholesterol, glucose).  
  - Create categorical plots and heatmaps for data exploration.  
- **Skills Demonstrated:** Data cleaning, feature engineering, visualization with Matplotlib and Seaborn, correlation analysis.

### 1.4 [Page View Time Series Visualizer](Project4_Page_View_Time_Series_Visualizer)
- **Objective:** Analyze time series data of daily page views on freeCodeCamp.org forum.  
- **Dataset:** Daily page views from May 9, 2016, to December 3, 2019.  
- **Key Tasks:**
  - Clean data and remove outliers.  
  - Create line plot, bar chart, and box plots to visualize trends and seasonality.  
- **Skills Demonstrated:** Time series analysis, data visualization, pattern recognition.

### 1.5 [Sea Level Predictor](Project5_Sea_Level_Predictor)
- **Objective:** Analyze global average sea level data and predict sea level changes through 2050.  
- **Dataset:** Global average sea level changes from 1880 to 2014.  
- **Key Tasks:**
  - Scatter plot of historical data.  
  - Linear regression using `scipy.stats.linregress` to predict future levels.  
  - Compare overall trends with post-2000 trends.  
- **Skills Demonstrated:** Time series analysis, linear regression, prediction, environmental data interpretation.

---

## 2. Skills Demonstrated Across Projects
- **Data Manipulation & Cleaning:** Pandas, NumPy, handling missing data, filtering, feature engineering.  
- **Data Visualization:** Matplotlib, Seaborn (line plots, bar charts, box plots, heatmaps).  
- **Statistical Analysis:** Mean, variance, standard deviation, percentages, correlation.  
- **Time Series Analysis:** Trend and seasonality analysis, linear regression predictions.  
- **Python Programming:** Functions, error handling, structured code, and testable scripts.  

---

## 3. How to Use
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/salahAlawieh/Python-Data-Analysis-Projects.git
2. Navigate to a project folder: cd Python-Data-Analysis-Projects/ProjectX_FolderName
3. Run the code: python main.py
4. Optional: Run unit tests to verify results: python test_module.py
