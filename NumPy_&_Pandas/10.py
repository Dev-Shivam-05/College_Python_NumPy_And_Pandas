from os import sysconf_names
# Load a CSV file and display only the names of students who scored more than 75 marks.

import pandas as pd

df = pd.read_csv("data.csv")

s_names = df[df["Marks"]>75]["Name"]

print(s_names)