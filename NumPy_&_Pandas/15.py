# Using loc, display:
# - All columns for the row with index 0.
# - A slice of rows and selected columns using labels.

emp =  { "Name" : ["Shivam","Nurul", "Jarir","Pratham","Abhii"] , "Dept":["IT", "HR","Sales","HR","Finance"], "Salary": [80000, 72000, 72000, 64000, 45000]}

df = pd.DataFrame(emp)

print(df)


print("******************")


row = df.loc[:0]

print(row)

print("******************")

col= df.loc[0:3,["Name","Dept"]]

print(col)