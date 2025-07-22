import pandas as pd

df=pd.read_csv("sales_data.csv")

df["Salesperson"]=df["Salesperson"].str.strip().str.title()
df["Region"]=df["Region"].str.strip().str.title()
df["Product"]=df["Product"].str.strip().str.title()

df.rename(columns={"Unit_Sold": "Units_Sold", "Units_Price": "Unit_Price"}, inplace=True)

df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors='coerce')
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors='coerce')
df["Revenue"] = pd.to_numeric(df["Revenue"], errors='coerce')

df.dropna(inplace=True)

pivot = df.pivot_table(index='Product', columns='Region', values='Revenue', aggfunc='sum')
average = df.pivot_table(index='Region', values='Units_Sold', aggfunc='mean')
report = df.pivot_table(index='Salesperson', values='Revenue', aggfunc='sum')
units_sold = df.pivot_table(index='Product', columns='Salesperson', values='Units_Sold', aggfunc='sum')

print("\n📊 Revenue by Product and Region:\n", pivot)
print("\n📉 Average Units Sold per Region:\n", average)
print("\n🧾 Revenue by Salesperson:\n", report)
print("\n📦 Units Sold by Product and Salesperson:\n", units_sold)
