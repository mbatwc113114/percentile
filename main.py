import numpy as np 
import pandas as pd

# these file contant pw result excl file which is converted from pdf
file = 'result.xlsx'

df = pd.read_excel(file)

# here we are converting data frame into dictonary of individual students
def convert_dic():
    data = dict()
    for i in range(0,1):
        try:
            # adding data to dic by key and dic
            data.update({f"{df['ID No.'][i]}":[
                                     'phy':df['Physics'][i],
                                     'chem':df['Chemistry'][i],
                                     'math':df['Mathematics'][i],
                                     'Name':df['Student Name'][i],
                                     'total':df['Total'][i],
                                     'air':df['AIR'][i]]})
        except Exception as e:
            print(i," faield")
            # its returning the data set of students
    return data
        

data = convert_dic()
# search data by stusent id

print(data['7303551'])
