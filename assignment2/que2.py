import pandas as pd

def function1():
    df = pd.read_csv('./ToyotaCorolla.csv', encoding='latin1')

#'./ToyotaCorolla.csv' file is having some fault or unicode  that's why we used encoding
    print(df)
function1()