import pandas as pd
import io
NewFile = pd.read_excel(r"C:\Users\liz62\Desktop\Personal File\New folder\Python learning\codes\example1.xlsx")
NewFile2 = pd.read_excel(r"C:\Users\liz62\Desktop\Personal File\New folder\Python learning\codes\example1.xlsx", index_col = 'MONTH ENDING')
#print(NewFile)
#打开文件时未指定index则会自动生成，所以存储时会增加一列index。
UpdatedFile = NewFile.set_index('MONTH ENDING') #不直接取代但是把输出的新data frame赋予新变量来存储
NewFile.set_index('MONTH ENDING', inplace = True) #在dataframe内直接指定column取代现有index
NewFile.to_excel(r"C:\Users\liz62\Desktop\Personal File\New folder\Python learning\codes\example2.xlsx")
UpdatedFile.to_excel(r"C:\Users\liz62\Desktop\Personal File\New folder\Python learning\codes\example3.xlsx")
NewFile2.to_excel(r"C:\Users\liz62\Desktop\Personal File\New folder\Python learning\codes\example4.xlsx")
