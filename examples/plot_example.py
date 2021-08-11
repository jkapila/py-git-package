"""
A Generic Example
=======================================
A very small aexample to create a plot
"""

import matplotlib.pyplot as plt
#%%
# Importing packages
import numpy as np


#%%
# Creating a a small data
x = np.arange(0, 11, 0.5)
y = np.sin(x)
print(y)

#%%
# now lets plot it
plt.plot(x, y, marker="o", linestyle="", label="a plot")
plt.show()
