# Access the value at row index 2 and column index 1 using iloc.

import numpy as np

emp =  { "Name" : ["Shivam","Nurul", "Jarir","Pratham","Harsh"] , "Dept":["IT", "HR","Sales","HR","Finance"], "Salary": [80000, 55000, 62000,64000,45000]}

df = pd.DataFrame(emp)

print(df)

print("*****************")

row = df.iloc[[2],[1]]

print(row)