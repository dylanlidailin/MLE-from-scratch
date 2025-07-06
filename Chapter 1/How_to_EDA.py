#%%
print("Hello World")

#%%
#create a function that takes a list of numbers and returns the sum of the numbers
def sum_list(x):
    return sum(x)

import numpy as np
import pandas as pd


# %%
admit_2 = pd.read_csv("../data/LogReg.csv")
print(admit_2.info())

# %%
# How to use 'rank'
admit_2['rank'] = admit_2['rank'].astype("category")   # here, we assign the newly-assigned vars
print(admit_2.info())

# %%
