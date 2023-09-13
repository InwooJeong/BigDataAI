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
# %matplotlib inline
import matplotlib.pyplot as plt

y = [1,2,3,4,5]
plt.plot(y)
plt.show()
# -

y = [13,16,15,18,16,17,16]
plt.plot(y)

y = [13,16,15,18,16,17,16]
plt.plot(range(len(y)),y);

x = ['Mon','Dien','Mit','Donn','Fri','Sam','Sonn']
y = [13,16,15,18,16,17,16]
plt.plot(x,y);

x = ['Mon','Dien','Mit','Donn','Fri','Sam','Sonn']
y = [13,16,15,18,16,17,16]
plt.plot(x,y);
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')

x = ['Mon','Dien','Mit','Donn','Fri','Sam','Sonn']
y1 = [13,16,15,18,16,17,16]
y2 = [17,14,17,16,15,15,14]
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')

x = ['Mon','Dien','Mit','Donn','Fri','Sam','Sonn']
y1 = [13,16,15,18,16,17,16]
y2 = [17,14,17,16,15,15,14]
plt.plot(x,y1,label='Sold')
plt.plot(x,y2,label='On Shelves')
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')
plt.legend(loc="upper left")

x = ['Mon','Dien','Mit','Donn','Fri','Sam','Sonn']
y1 = [13,16,15,18,16,17,16]
y2 = [17,14,17,16,15,15,14]
plt.plot(x,y1,label='Sold')
plt.plot(x,y2,label='On Shelves')
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')
plt.legend(loc="upper left")
plt.title('Le Petit Prince: Sold & Left')

x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y,'bo')  # blue 색상의 o 모양 점
plt.show()

# +
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y,'bo')
plt.axis([0,6,0,30])
plt.show()

# axis -> x축과 y축 범위 지정 x: 0 ~ 6, y : 0 ~ 30
# -

import numpy as np
points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])
import matplotlib.pyplot as plt
plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1],"bo")

x = np.linspace(0,5,10)
y = x**2
plt.plot(x,y)

x = np.linspace(0,10,20)
y = x**2.0
plt.plot(x,y,"bo-",linewidth=3,markersize=5);

plt.plot(x,y,"gs-",linewidth=1,markersize=3);

x = np.linspace(0,10,20)
y1 = x ** 2.0
y2 = x ** 1.5
plt.plot(x,y1,"bo-",linewidth=2,markersize=12,label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12,label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5,10.5,-5,105])
plt.legend(loc="upper left")
plt.savefig("mplot.pdf")

x = np.logspace(-1,1,20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x,y1,"bo-",linewidth=2,markersize=12,label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12,label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5,10.5,-5,105])
plt.legend(loc="upper left")
plt.savefig("mplot.pdf")

import matplotlib.pyplot as plt
import numpy as np
x = np.random.standard_normal(size=1000)
plt.hist(x)

plt.hist(x, density=True)

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.hist(x)

# +
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(30)
y = np.random.rand(30)
colors = np.random.rand(30)
size = np.pi * (np.random.rand(30)*20)**2
plt.scatter(x,y, s=size, c=colors, marker='*', alpha=0.7)  # 산점도
plt.show()
