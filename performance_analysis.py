#import pandas to start
import pandas as pd

#convert it in dataframe and load the csv file
df = pd.read_csv("student_extended.csv")
print(df)

#arrange by class and gender
arrange_class = df.groupby(["Class", "Gender"])[["Math", "English"]].mean()
print(round(arrange_class, 2))

#min, max and count per group
sorting_students = df.groupby(["Class", "Gender"])[["Math", "English"]].agg(["min", "max", "count"])
print(sorting_students)