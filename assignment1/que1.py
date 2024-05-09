import numpy as np
import pandas as pd
def function1():
    emp_id = [1,2,3,4,5,6,7,8,9,10]
    names = ['praju','sumi','raju','anu','anshu','kalu','chintu','goli','krish','piyu']
    emp_names = pd.Series(names, index= emp_id)
    print(f"following are the employees = ")
    print(emp_names)
    print(f"type of emp_names series = {type(emp_names)}")

    # df = pd.DataFrame([
    #     [1,2,3,4,5,6,7,8,9,10],
    #     ['praju','sumi','raju','anu','anshu','kalu','chintu','goli','krish','piyu']
    # ])
    # print(df)
    print('_'* 100)
    df = pd.DataFrame(emp_names, columns=['names'])
    print("all records")
    print(df)
    print('_'* 100)

    print(df.head())
    print('_'* 100)

    print(df.tail())
    df.to_csv('MYRECORD.csv', index_label='emp_id')


function1()