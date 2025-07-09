import pandas as pd
#load csv
df = pd.read_csv("product_sales.csv") 

#Calculate total revenue column
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

#Summary Calculation
total_revenue = df["Revenue"].sum()
best_seller = df.loc[df["Units_Sold"].idxmax()]["Product"]
average_units = df["Units_Sold"].mean()

#Print Results
print("\n📊 Product Sales Summary")
print("----------------------------")
print(df)
print(f"\n💰 Total Revenue: ${total_revenue:.2f}")
print(f"🏆 Best Seller: {best_seller}")
print(f"📈 Average Units Sold: {average_units:.2f}")

