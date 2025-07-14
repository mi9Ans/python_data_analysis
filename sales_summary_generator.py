import pandas as pd
df = pd.read_csv("product_info.csv")
print(df)

total_sales = df["Units Sold"].sum()
print(total_sales)

top_product = df[df["Units Sold"] == df["Units Sold"].max()]
print(top_product)

average = df["Units Sold"].mean()
print(round(average, 2))

sort_sales = df.sort_values(by = "Units Sold", ascending = False)
print(sort_sales)


