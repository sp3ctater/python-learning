import pandas as pd

L1  = [100,200,300]
L2  = ['x','y','z']

s1 = pd.Series(L1,index = L2)
print(s1)

s2 = pd.Series([1,2,3],index = [1,2,3],name='A')
s3 = pd.Series([10,20,30],index = [1,2,3],name='B')
s4 = pd.Series([100,200,300],index = [1,2,3],name='C')

df = pd.DataFrame({s2.name:s2,s3.name:s3,s4.name:s4})
print(df)

df = pd.DataFrame([s2,s3,s4])
print(df)

s2 = pd.Series([1,2,3],index = [1,2,3],name='A')
s3 = pd.Series([10,20,30],index = [1,2,3],name='B')
s4 = pd.Series([100,200,300],index = [2,3,4],name='C')

df = pd.DataFrame([s2,s3,s4])
print(df)