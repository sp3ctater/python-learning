import pandas as pd

books = pd.read_excel('C:/Temp/Books.xlsx', index_col='ID')

books.['Price'] = books.['ListPrice']*books['Discount']

for i in books.index:
    books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]

for i in range(5,16):
    books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]

def add_2(x):
    return x +2

books['ListPrice']= books['ListPrice'].apply(add_2)
books['ListPrice']= books['ListPrice'].apply(lambda x: x+2)

