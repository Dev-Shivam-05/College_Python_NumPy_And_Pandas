# Create a DataFrame using the dictionary: {Product;: [Pen, Notebook, Eraser],Price:
# [10, 25, 5], Stock: [100, 50, 200]}. Print the entire DataFrame..

import pandas as pd

data = {'Product': ['Pen', 'Notebook', 'Eraser'],
        'Price': [10, 25, 5],
        'Stock': [100, 50, 200]
        }

df = pd.DataFrame(data)

print(df)