import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv') 

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.drop_duplicates()

# Numerical Columns Cleaning
df['price'] = df["price"].astype(str).str.replace(",", "").astype(float)
df['area'] = df["area"].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)


# Categorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

df = df.drop_duplicates()

print(df)
print(df.info())

# Question 1: Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat in the dataset is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} Crores. It has an area of {costliest_flat['area']} sqft and a rate per sqft of {costliest_flat['rate_per_sqft']}. The flat is currently {costliest_flat['status']} and is built by {costliest_flat['builder_name']}. It is not approved by RERA.")

# Question 2: Which locality has the highest average price?
avg_price_by_locality = df.groupby('locality')['price'].mean().sort_values(ascending=False)
print(f"The locality with the highest average price is {avg_price_by_locality.idxmax()} with an average price of {avg_price_by_locality.max()/10000000:.2f} Crores.")

# Question 3: Which locality has the highest average price per square foot?
avg_rate_by_locality = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False)
print(f"The locality with the highest average price per square foot is {avg_rate_by_locality.idxmax()} with an average price per square foot of {avg_rate_by_locality.max():.2f}.")

#  question 4: Do ready-to-move properties cost more then under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more than average then under-constuction properties.")
else:
    print("Under-construction properties cost more than average then ready-to-move properties.")

# Question 5: Do RERA-approved  properties command a price premium ?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print("RERA-approved properties command a price premium.")
else:
    print("RERA-approved properties do not command a price premium.")

# Question 6: How does area (Sqft) impact property price?
plt.figure(figsize=(8, 5))
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

# Question 7: Which BHK configuration is most expensive bassed on per sqft rate?
avg_rate_by_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {avg_rate_by_bhk} BHK.")

# Question 8: Which flat type is the contliestn?
avg_price_by_flat_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest flat type on average is {avg_price_by_flat_type}.")

# Question 9: Do certain builders price higher ?
avg_price_by_builder = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
print(avg_price_by_builder)

# Question 10: Are larger homes more expensive per sqft?
plt.figure(figsize=(8, 5))
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Sqft')
plt.xlabel('Area')
plt.ylabel('Rate per Sqft')
plt.show()
