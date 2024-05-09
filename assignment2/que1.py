import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def function1():
    df = pd.read_csv('./Engine.csv')
    print(df)

    print(df.head())
    print('-' * 80)

    print(df.tail(10))
    print('-' * 80)

    df.info()
    print('-' * 80)

    print(df.describe())
    print('-' * 80)



# function1()

def function2():

    df = pd.read_csv('./Engine.csv')
    # print(df)
    # print(df.isna())
    # print(df.isna().any())
    print(df.isna().sum())


# function2()

def function3():
    df = pd.read_csv('./Engine.csv')
    print(df)
plt.figure(figsize=(10, 6))
plt.bar('ENGINESIZE',2, 0.1, data=None)
plt.xlabel('Engine Size')
plt.ylabel('CO2 Emissions')
plt.title('Engine Size vs CO2 Emissions')
plt.show()
function3()
