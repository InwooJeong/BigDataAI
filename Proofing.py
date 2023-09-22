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
