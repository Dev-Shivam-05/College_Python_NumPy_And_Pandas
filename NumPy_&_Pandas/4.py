# Create a list of integers from 1 to 10. Convert it into a NumPy array and apply all five
# statistical functions.

import numpy as np
import scipy 
import statistics as stats
list = [1,2,3,4,5,6,7,8,9,10]
print(list)

print(f"The Mean of The List is :- {np.mean(list)}")
print(f"The Median of The List is :- {np.median(list)}")
print(f"The Standard Daviation of The List is :- {np.std(list)}")
print(f"The Variance of The List is :- {np.var(list)}")