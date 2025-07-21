import pandas as pd

data = {
    "Name": ["  Rahul", "Sneha", "Amit", "Sneha", "  Riya", "Nikhil", "Priya", "Riya"],
    "Subject": ["Math", "Science", "Math", "Math", "Science", "Math", "Science", "Science"],
    "Score": ["85", " ", "78", "85", "91", "eighty", "88", "91"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Delhi", "Bangalore", " "],
    "Gender": ["M", "F", "M", "F", "F", "M", "F", "f"]
}
df = pd.DataFrame(data)

print(df)
df["Name"]=df["Name"].str.strip().str.title()
df["Subject"]=df["Subject"].str.strip()
df["Score"]=df["Score"].str.strip()
df["City"]=df["City"].str.strip()
df["Gender"]=df["Gender"].str.strip()

df["Gender"]=df["Gender"].replace({
    'M':'Male',
    'F':'Female',
    'f':'Female'
})

df["Score"]=pd.to_numeric(df["Score"], errors='coerce')

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

avg_score=df["Score"].mean()
unique_student=df["Name"].nunique()
count_student=df["Subject"].value_counts()
top_science_scorer = df[df["Subject"] == "Science"].loc[df[df["Subject"] == "Science"]["Score"].idxmax()]
common_city=df["City"].value_counts().idxmax()
avg_score_per_subject=df.groupby("Subject")["Score"].mean()

print("📃 Cleaned Data:\n", df)
print("\n📊 Average Score :", round(avg_score, 2))
print("Unique Students :", unique_student)
print("🗄️Student per Subject :\n", count_student)
print("🏆 Top Scorer in Science :\n", top_science_scorer)
print("📉 Average Score per Subjects :\n", round(avg_score_per_subject, 2))
print("🌆 Most Common City :", common_city)
