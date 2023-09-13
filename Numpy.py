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
# Numpy 기초 - import문으로 모듈을 가지고와 해당 데이터를 Numpy 형식으로 수정 후 작업

import numpy as np

x = np.array([1,3,5])
print(x.mean())
# -

print(x.shape)

a = np.array([[1,2,3],[2,3,4]])
print(a.shape)

x = np.array([1,3,5,7,9,11]).reshape(3,2)
print(x)

y = np.ones([3,4])
print(y)

x = np.array([[1,3,5],[2,4,6]])
print(x[1])
print(x[1].mean())
print(x.mean())
print(x.shape)

list1 = [[1,11],[2,12],[3,13]]
print(list1[1][1])

# +
# Numpy 배열 슬라이싱

# 목표 : 11,12,13만 출력
list1 = [[1,11],[2,12],[3,13]]

# 원치 않는 결과
print(list1[:][1])
# X! Error
# print(list1[:,1])

# +
# 파이썬 2차원 리스트를 Numpy 배열로 변환 후 출력

import numpy as np
list1 = [[1,11],[2,12],[3,13]]
np_ary = np.array(list1)

# print(np_ary)
print(np_ary[:, 1])

# +
# print(np.array(list1[:,1]))
# Numpy 변환 전에 슬라이스 ->  에러 발생
# -

list1 = np.array([[1,11],[2,12],[3,13]])
print(list1[:,1])

list1 = [[1,11],[2,12],[3,13]]
print(np.array(list1[:][0]))

# +
# Numpy 연산
import math
math.sqrt(2)

# math.sqrt([2,3,4])
# -

import numpy as np
np.sqrt([2, 3, 4])

import numpy as np
a = np.arange(15)
print(a)

import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print(a[1:2,1])

# +
# 제로 벡터와 제로 행렬

import numpy as np
zero_vector = np.zeros(3)
print(zero_vector)
# -

zero_matrix = np.zeros((4,3))
print(zero_matrix)

zero_vector = np.zeros(5)
print(zero_vector)

# 생성한 벡터나 행렬에 새로운 값으로 다시 재설정 가능
import numpy as np
my_array = np.zeros(15).reshape(3,5)
my_array += 4
my_array

# +
# 전치행렬(Transpose Matrix)

ary = [[1,2],[3,4]]
# print(ary.transpose())
# -> transpose가 없음
# -

import numpy as np
ary = np.array([[1,2],[3,4]])
print(ary.transpose())

x = [1,2,3]
y = [4,5,6]
z = x + y
print(z)

# +
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x + y

print(z)
print(x*y)
# +
# s = [1,2,3]
# t = s + 1
# print(t)

# 에러 발생 -> 3개 원소로 구성된 1차원 배열에 1을 더할 수 없음
# -


s = np.array([1,2,3])
t = s + 1
print(t)

x = np.array([4,8,12])
y = np.array([2,4,6])
z = x/y
print(z)

X = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(X[1])  # [4 5 6] 출력 -> X배열 인덱스 1번 내용을 출력
print(X[:,1])  # [2 5 8] 출력 -> 각 1차원 배열 1번 내용 출력

# +
# 2개의 Numpy 배열 간 계산도 가능

X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(X[:,1]+Y[:,1])
# -

a = np.array([10,20,30,40,50,60,70])
i = [1,3,5]
print(a[i])

# +
a = np.array([10,20,30,40,50,60,70])
b = a[1:6:2]
print('b:', b)
b[1] = 10
print('b:', b)
print('a:', a)

# 배열 a를 슬라이싱으로 복사한 배열 b를 Numpy 변환 후 수정해도 a에 영향 x

# +
# Numpy Boolean

a = np.array([10,20,30,40,50,60,70])
b = a > 50
print(b)
# -

ary = np.random.random(5)
print(ary)
print(np.all(ary >= 0.3))
print(np.any(ary > 0.7))

# +
height = [173, 168, 171, 189, 179]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
# bmi = (weight/(height**2))*10000

import numpy as np

height = np.array(height)
weight = np.array(weight)
bmi = (weight/(height**2))*10000
print(bmi)
chk = bmi > 21
print(chk)

# +
# 등간격 나누기

# linspace -> 사이 값들을 선형적으로 분배
np.linspace(0,12,4)
# -

np.linspace(0,12,4,retstep=True)

np.linspace(0,12,3)

np.linspace(0,12,3,endpoint=False)
# endpoint가 false -> 우선 4개 구간으로 나누고 마지막 값을 제외하려 출력. default 값은 true

# +
# logspace -> 사이 값들을 대수(로그) 형태 간격으로 분배

np.logspace(np.log10(10),np.log10(100),5)
# -

np.logspace(1,2,5)
