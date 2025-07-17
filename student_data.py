#Import pandas to get started
import pandas as pd

#Load Data
df=pd.read_csv("student_survey_dirty.csv")

#remove fully empty rows
df.dropna(how='all', inplace=True)

#View initial data
print(df.head())
print(df.info())

# Clean Age: replace blanks, convert to Int64, fill missing with rounded mean
df['Age']=df['Age'].replace([' ', '', '  '], pd.NA)
df['Age']=df['Age'].astype('Int64')
df['Age'].fillna(round(df['Age'].mean()), inplace=True)

# Clean Gender: standardize text, map to Male/Female
df['Gender']=df['Gender'].str.strip().str.lower()
df['Gender']=df['Gender'].replace({
    'm':'Male', 'M': 'Male', 'male': 'Male',
    'f':'Female', 'F':'Female', 'female': 'Female'
})
#Clean Name formatting 
df['Name']=df['Name'].str.strip().str.title()

#Remove Duplicates
df.drop_duplicates(inplace=True)

#Display Insights
print(df['Gender'].value_counts())
print("Unique Cities:", df['City'].nunique())
print(df)
