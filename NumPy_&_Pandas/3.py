# Calculate the mean, median, mode, standard deviation, and variance for the array: 
# [12, 15, 12, 18, 21, 24, 24, 24, 27, 30]

import numpy as np
import scipy 
import statistics as stats
list = [12, 15, 12, 18, 21, 24, 24, 24, 27, 30]
print(list)

print(f"The Mean of The List is :- {np.mean(list)}")
print(f"The Median of The List is :- {np.median(list)}")
print(f"The Standard Daviation of The List is :- {np.std(list)}")
print(f"The Standard Daviation of The List is :- {np.var(list)}")