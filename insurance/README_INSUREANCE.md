# Data Things

Data cleaning, analysis and machine learning on real datasets.

---

## File names

| File | Topic | Description |
|------|-------|-------------|
| `insurance_cleaning.py` | Data Cleaning | |
| `insurance_regression.py` | Machine Learning | |
| `insurance_uncleaned.csv` | Dataset | Raw data |
| `insurance_cleaned.csv` | Dataset | Cleaned data |

---

## Insurance Dataset

**Files:** `insurance_cleaning.py`, `insurance_regression.py`  
**Concepts:** Data cleaning, Pandas, One-hot encoding, Linear Regression

**Why this project:**  
Just wanted to learn basic data handling with pandas so downloaded this dataset.
Cleaning took way longer than I expected.

**What was wrong with the data:**
- The types of the columns were different
- There were about 132 missing values
- Columns like smoker and gender were in strings with corrupted and mismatched data
- There were 4 regions for which the data was collected but were in a single column

**Cleaning approach:**
- Converted columns of smoker and sex to boolean values (1 and 0) (if male then 0 else 1)(if smoker then 1 else 0) for which I parsed through all the strings in the column and checked for the first letter of the words (if m then male if f then female)
- Columns like number of children had negative values so converted negative values to absolute values, also had to strip charges for $ sign since some entries had $ attached to them
- Had to use hot coding for the regional data so region column was replaced with 4 new columns for each of the 4 distinct regions then filled 1 for true
- Filled the missing values with mode for data like number of children, smoker, median for charges, age and mean for BMI (since median would not skew the data)

**Regression results:**  
Abysmal R² score of 0.53

**Reason:**  
Meddling with the data and filling NaN values with mean, median, mode even though 
I did put a thought as to why those measures were suitable.

**Note:**  
> Cleaning the data is the main part. Drop NaN values if possible, fill only if necessary.
