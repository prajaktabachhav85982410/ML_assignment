import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the data
df = pd.read_csv('./East_std.csv')
print(df)
print('-' * 100)
#exploratory data analysis

df.info()
print('-' * 100)

df.dropna(inplace = True)
df.info()

