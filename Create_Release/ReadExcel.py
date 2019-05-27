#!/usr/bin/python

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np 
import os #The inclusion of this library was due to the need of execute commands in the system

#Reading excel with pandas, only List sheet
df = pd.read_excel('ReleaseObjectCheckList.xlsx', sheet_name='List')

#Print excel columns
#print("Column headings")
#print(df.columns)

#Select only the rows with values
df2 = pd.DataFrame(df)
Script_Name = df2[df2['script name'] != np.nan]

#print(Script_Name['script name'])

#Create a new column with the command to copy of items in the release folder
df2['command'] = 'cp ' + df['script path'] + '/' + df['script name'] + ' ' + df['target']

#Print new column
print('\n \n')
print( df['command'] )
print('\n \n')

#Print DataFram with the new column
print(df)
print('\n\n')

#Create release_log
f = open("release_log.txt","w+")

#When it doesn't exist scripts in release folder the output the query doesn't found the folder
os.system('rm -r /Users/gustavopaez/Documents/Python_Scripts/create_release/release/folder1/*')
print("\n :::::::: clean release/folder1 \n")
os.system('rm -r /Users/gustavopaez/Documents/Python_Scripts/create_release/release/folder2/*')
print("\n :::::::: clean release/folder2 \n")

#Iteration per row of the DataFrame
for index_row, row in df2.iterrows():
    print('Execution: ' + str(index_row) + ' ' + row.iloc[-1])
    f.write('\n\n Execution: ' + str(index_row) + ' ' + row.iloc[-1])
    os.system(str(row.iloc[-1]))
    print('\n')
print('\n')
