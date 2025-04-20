# Create a DataFrame with at least 5 rows and 3 columns.
# - Retrieve the third row using iloc.
# - Retrieve the values from the second and fourth rows, and the first two columns using
# iloc.

emp =  { "Name" : ["Shivam","Nurul", "Jarir","Pratham","Abhii"] , "Dept":["IT", "HR","Sales","HR","Finance"], "Salary": [80000, 79999, 72000,64000,45000]}

df = pd.DataFrame(emp)

print(df)

print("******************")

row = df.iloc[3,:]

print(row)

row = df.iloc[[2,4],[0,1]]

print(row)

