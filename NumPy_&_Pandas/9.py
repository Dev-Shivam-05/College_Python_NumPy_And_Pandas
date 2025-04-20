# Create a sample data.csv file with student details (Name, RollNo, Marks) and:
# - Read it using pd.read_csv().
# - Print the total number of students.

import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print(df.count())