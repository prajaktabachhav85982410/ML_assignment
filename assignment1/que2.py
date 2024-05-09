import pandas as pd

def function1():
    df = pd.read_csv('./Advertising.csv')
    print(df)
    print('-' * 100)
    print(df.head())
    print('-' * 100)
    print(df.tail())
    print('-' * 100)
    print(f"columns = {df.columns}")
    print('-' * 100)
    print(df.tail(3))
    print('-' * 100)

    df.info()
    print('-' * 100)

    print(df.dtypes)
    print('-' * 100)

    print(df.isna().sum())
    print(df.dropna())
    print('-' * 100)


    df.drop('radio',axis = 1, inplace = True)
    print(df.isna().sum())
    print(df.shape)
    print(df.head(10))
    df['updated_sales '] = df['sales']*1.10
    print(df)

    print(df.shape)
function1()