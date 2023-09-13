# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Series(1차원)와 Data Frame(2차원) 형태

# 1.Series
# 복수의 행으로 이루어진 하나의 열 구조. 색인을 가지고 원하는 데이터에 접근 가능
import pandas as pd
pd.Series([7,3,5,8])

# +
# 색인은 설정 가능
x= pd.Series([7,3,5,8],index=['서울','대구','부산','광주'])
print(x)

# index로 검색 가능
x[['서울','대구']]
# -

# index/데이터만 출력
x.index

x.values

# +
# sorted 함수
print(sorted(x.index))
print(sorted(x.values))

x = x.reindex(sorted(x.index))
x

# +
x = pd.Series([3,5,8,9], index=['서울','대구','부산','광주'])
y = pd.Series([2,4,5,1], index=['대구','부산','서울','대전'])
x + y

# x와 y에 공통된 인덱스가 조냊해야 더할 수있다. 광주, 대전 - NaN
# -

medal = [1,3,2,4,2,3]
x = pd.Series(medal)
print(pd.unique(x))

medal = ['민준','현우','서연','동현','서연','현우']
x = pd.Series(medal)
print(pd.unique(x))

# +
# dictionary -> pandas series

age = {'민준':23, '현우':43, '서연':12, '동현':45}
x = pd.Series(age)
x

# +
names = ['민준','서연','현우','민선','동현','수빈']
pdata = pd.Series(names)
print(pdata)

a = pdata[3:6]
print(a.values)
# print(a[2])
print(a)

# index까지 가지고 가버림 -> 배열 index와 다르다.

# +
# 2. DataFrame
# 행과 열을 가지고 보통 열에 각각의 이름을 부여한다.

data = {'age':[23,43,12,45],
       'name':['민준','현우','서연','동현'],
       'height':[175.3,180.3,165.8,172.7]}
x = pd.DataFrame(data,columns = ['name','age','height'])
x
# -

x.name

ary = [[1,2],[3,4],[5,6]]
data = pd.DataFrame(ary, columns=['First','Second'])
data

data.iloc[1]

data.iloc[:,-1]

ary = [[1,2],[3,4],[5,6],[7,8],[9,10]]
data = pd.DataFrame(ary, columns=['First','Second'])
data.head(3)

data.tail(3)

# +
ary = [[1,2],[3,4],[5,6],[7,8],[9,10]]
data = pd.DataFrame(ary, columns=['First','Second'])
bools = [False, True, True, False, True]
data.Second[bools]

# Second에 속하며 bools가 True에 해당
# -

print(x.mean(axis=0))

data = {'age':[23,43,12,45],
       'name':['민준','현우','서연','동현'],
       'height':[175.3,180.3,165.8,172.7]}
x = pd.DataFrame(data,columns = ['name','age','height'])
index = [True,False,True,False]
print(x[index])

# +
# Pandas DataType
# Objects : 문자 / 문자열
# Int64 : 정수
# Float64 : 실수

# +
import pandas as pd
import numpy as np

ary = [[1,2],[3,4],[5,6],[7,8],[9,10]]
data = pd.DataFrame(ary,columns=['수온','상온'])
data
# -

data['수온'] = data['수온'].astype('float')
data
