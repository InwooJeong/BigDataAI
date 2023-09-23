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
import pandas as pd
import numpy as np
from numpy import NaN

data = pd.DataFrame(np.arange(12).reshape(3,4),columns=['A','B','C','D'])

data.D[2] = 'NaN'
data
# -

data.drop(['D'],axis=1)

robots = [[24,23680],[35,NaN],[46,47350],[27,NaN]]
print(robots)
# numpy에서 NaN을 import해서 사용 가능

data = pd.DataFrame(robots,columns=['max_speed','price'])
print(data)

data.dropna(subset=['price'],axis=0,inplace=True)  # dropna -> NaN이 들어있는 행 삭제. 
# axis=0 -> 행 삭제 inplace=True -> 데이터 세트 자체 수정
print(data)

# +
robots = [[24,23680],[35,NaN],[46,47350],[27,NaN]]
data = pd.DataFrame(robots,columns=['max_speed','price'])

mean = data['price'].mean()
data.replace(NaN,mean)
print(data)
# -

# data = data.replace(NaN, mean)
data.replace(NaN,mean,inplace = True)
print(data)

import matplotlib.pyplot as plt
x = np.random.randn(1000)
plt.hist(x, density=True, bins=np.linspace(-5,5,21))

# ### 1. Simple Feature Scaling
#
# Xnew = Xold / Xmax
#
#
# ### 2. Min - Max
#
# Xnew = Xold - Xmin / Xmax - Xmin
#
#
# ### 3. Z - score
#
# Xnew = Xold - feature의 평균 / 표준편차

# # Data Formatting
# - 수치값을 카테고리 값으로 변환

price = np.random.randint(100,size=8)*10000
cars = pd.DataFrame(price,columns=['price'])
cars

group_names = ['저급','중급','고급']
cars['Level'], mybin = pd.cut(cars['price'],3,labels=group_names,retbins=True)
cars

print(mybin)

# - 카테고리 값을 수치값으로 변환

ary = [[1,1.1,'손'],[2,2.2,'날개'],[3,3.3,'손']]
data = pd.DataFrame(ary,columns=['수온','상온','hand'])
pd.get_dummies(data['hand'])

data = pd.concat([data,pd.get_dummies(data['hand'])],axis=1,sort=False)
data

data.drop(['hand'],axis=1,inplace=True)
data
