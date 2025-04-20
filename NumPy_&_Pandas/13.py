# Use loc to get the rows where Salary &gt; 50000.

import pandas as pd
emp =  { "Name" : ["Shivam","Nurul", "Jarir","Pratham","Abhii"] , "Dept":["IT", "HR","Sales","HR","Finance"], "Salary": [80000, 45000, 72000,64000,45000]}

df = pd.DataFrame(emp)

print(df)

print("--------------------")

row = df[df["Salary"]>50000]

print(row)
