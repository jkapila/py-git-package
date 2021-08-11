"""
A Generic Example
=======================================
A very small aexample to create a plot
"""
#%%
# Importing packages
import matplotlib.pyplot as plt
import numpy as np


#%%
# Creating a a small data
x = np.arange(0, 11, 0.01)
y = np.sin(x)
print(y[:10])

#%%
# now lets plot it
plt.plot(x, y, marker="o", linestyle="", label="a plot")
plt.show()
