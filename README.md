# 🏠 Gurugram Real Estate Data Analysis

## 📌 Project Overview

This project performs Data Cleaning and Exploratory Data Analysis (EDA) on a Gurugram Real Estate dataset using Python.

The objective is to analyze:

- Property pricing trends
- Locality-based price variation
- Builder pricing strategy
- BHK configuration impact
- RERA approval impact
- Area vs Price relationship

---

# 📂 Dataset Information

After cleaning:

- Total Records: 14,223
- Total Columns: 12
- Memory Usage: ~1.3 MB

## Columns in Dataset

1. price (float)
2. status (object)
3. area (int)
4. rate_per_sqft (int)
5. property_type (object)
6. locality (object)
7. builder_name (object)
8. rera_approval (bool)
9. bhk_count (int)
10. society (object)
11. company_name (object)
12. flat_type (object)

---

# 🧹 Data Cleaning Performed

- Standardized column names (lowercase, removed spaces)
- Removed duplicate rows
- Cleaned price column (removed commas, converted to float)
- Cleaned area column (converted to integer)
- Cleaned rate_per_sqft column
- Standardized categorical values (status, flat_type)
- Converted RERA approval to Boolean (True/False)

---

# 📊 Analysis & Results

## 1️⃣ Costliest Property

- Flat Type: Apartment  
- Locality: Sector 42  
- Price: 122.63 Crores  
- Area: 16,500 sqft  
- Rate per Sqft: 74,323  
- Status: Ready to Move  
- Builder: Provident Capital  
- RERA Approved: No  

---

## 2️⃣ Highest Average Price by Locality

- Locality: Baliawas  
- Average Price: 58.33 Crores  

---

## 3️⃣ Highest Average Rate per Sqft by Locality

- Locality: Sector 42  
- Average Rate per Sqft: 55,989  

---

## 4️⃣ Ready-to-Move vs Under-Construction

Result:

Ready-to-move properties cost more on average than under-construction properties.

Insight:

Buyers are willing to pay a premium for immediate possession.

---

## 5️⃣ RERA Approval Impact

Result:

RERA-approved properties do NOT command a price premium.

Insight:

Approval ensures compliance but pricing is more influenced by location and builder brand.

---

## 6️⃣ BHK Configuration Analysis

Result:

114 BHK appears as the most expensive configuration based on average rate per sqft.

Note:

This is likely a data anomaly and requires validation.

General Trend:

Higher BHK → Higher total price.

---

## 7️⃣ Costliest Flat Type

Result:

Villa is the most expensive flat type on average.

Insight:

Luxury segment drives premium pricing in the market.

---

## 8️⃣ Builder Pricing Strategy

Top 5 Builders based on Average Rate per Sqft:

1. Camelliaass – 44,724
2. Cameliaas – 40,000
3. Tulip – 28,571
4. Prom – 27,358
5. Magnoliaass – 26,666

Insight:

Certain builders follow a premium pricing strategy.

---

## 9️⃣ Area vs Price Relationship

Observation:

- Area directly impacts total property price.
- Larger homes have higher overall cost.
- Rate per sqft does not always increase proportionally with area.

Luxury properties show nonlinear pricing behavior.

---

# 📈 Key Business Insights

- Location is the strongest price driver.
- Luxury flat types (Villa) command highest pricing.
- Builder brand value impacts rate per sqft.
- Ready-to-move properties attract higher buyers.
- Dataset anomalies should be validated before business decisions.

---

# 🛠 Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# 🚀 Conclusion

This project demonstrates how real estate pricing depends on multiple factors:

- Locality
- Builder reputation
- Property type
- BHK configuration
- Area

The analysis helps:

- Investors identify premium segments
- Developers understand pricing trends
- Buyers evaluate market positioning

---

# 👨‍💻 Author

Rohit Kumar 
Gurugram Real Estate Data Analysis Project
