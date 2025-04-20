# Print the first and last rows of the DataFrame using .head() and .tail().

import pandas as pd

df = pd.read_csv("data.csv")

print(df.head(3))
print(df.tail(3))