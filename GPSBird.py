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
import matplotlib.pyplot as plt
import numpy as np

import datetime as dt

bird = pd.read_csv('bird_tracking.csv')
bird.columns
# -

bird.date_time[0:3]

ix = bird.bird_name == "Sanne"
date = bird.date_time
print(date[:1])

ix = bird.bird_name == "Sanne"
date = bird.date_time
print(date[-1:])

dt.datetime.today()

time1 = dt.datetime.today()

time2 = dt.datetime.today()
time2 - time1

date_str = bird.date_time[0]
print(date_str)

date_str[:-3]

a = dt.datetime.strptime(date_str[:-3],'%Y-%m-%d %H:%M:%S')
print(a)

timestamps = []
for k in range(len(bird)):
    timestamps.append(dt.datetime.strptime(bird.date_time.iloc[k][:-3],'%Y-%m-%d %H:%M:%S'))
timestamps

bird['timestamp'] = pd.Series(timestamps,index=bird.index)
bird.timestamp[1]-bird.timestamp[0]

a = bird.timestamp[1]-bird.timestamp[0]
print(a)

bird.index

bird.head()

bird_names = pd.unique(bird.bird_name)
print(bird_names)

# +
timestamps = []
for k in range(len(bird)):
    timestamps.append(dt.datetime.strptime(bird.date_time.iloc[k][:-3],'%Y-%m-%d %H:%M:%S'))
bird['timestamp'] = pd.Series(timestamps,index=bird.index)

times = bird.timestamp[bird.bird_name=='Eric']
elapsed = [time-times[0] for time in times]
elapsed[100]
# -

print(elapsed[0])
print(elapsed[1])
print(elapsed[100])

elapsed[100]/dt.timedelta(days=1)

elapsed[100]/dt.timedelta(hours=1)

plt.plot(np.array(elapsed)/dt.timedelta(days=1))
plt.xlabel('Observation')
plt.ylabel('Elapsed(days)')

ix = bird.bird_name == "Eric"
speed = bird.speed_2d[ix]
print(speed.head())

plt.plot(range(50),speed[:50]);
plt.xlabel('Observation')
plt.ylabel('Flying Speed');

speed = bird.speed_2d[bird.bird_name=='Nico']
plt.plot(range(50),speed[:50])
plt.xlabel('Observation')
plt.ylabel('Flyingspeed')

speed = bird.speed_2d[bird.bird_name=='Eric']
speed[218]

speed[219]

speed = np.array(speed)
print(np.isnan(speed))

np.isnan(speed).any()


def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n):
            return i


ind = getnan(speed)
print(ind)

len(np.isnan(speed))

nanlist = []
def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n):
            nanlist.append(i)


getnan(speed)
print('nan의 총 개수 : ', len(nanlist))
print(nanlist)

import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':');

# +
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))

for name in bird_names:
    ix = bird['bird_name']==name
    x, y = bird.longitude[ix],bird.latitude[ix]
    ax.plot(x,y,'.',transform=ccrs.Geodetic(),label=name)
    
plt.legend(loc='upper left')

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':');
# -

x,y = bird.longitude, bird.latitude
plt.figure(figsize=(7,7))
plt.plot(x,y,'.');

ix = bird.bird_name == "Eric"
x,y = bird.longitude[ix],bird.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x,y,'.');

# %matplotlib inline
from scipy.spatial import distance
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':');
bird_names = pd.unique(bird.bird_name)
ix = bird['bird_name'] == 'Eric'
x,y = bird.longitude[ix], bird.latitude[ix]
ax.plot(x[0:17000],y[0:17000],'.', transform=ccrs.Geodetic());                # 남하
ax.plot(x[17101:18600],y[17101:18600],'.', transform=ccrs.Geodetic());        # 북상

# +
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':');

def euc(a,b):
    return distance.euclidean(a,b)
bird_names = pd.unique(bird.bird_name)

sindex = 2500
eindex = 7500

ix = bird['bird_name'] == 'Eric'
x,y = bird.longitude[ix], bird.latitude[ix]

i = [x[sindex],y[sindex]]
j = [x[eindex],y[eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Eric',euc(i,j))

ix = bird['bird_name'] == 'Nico'
x,y = bird.longitude[ix], bird.latitude[ix]
start = len(x)
dest = len(y)

i = [x[start+sindex],y[start+sindex]]
j = [x[dest+eindex],y[dest+eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Nico',euc(i,j))

ix = bird['bird_name'] == 'Sanne'
x,y = bird.longitude[ix], bird.latitude[ix]
start = start+len(x)
dest = dest+len(x)

i = [x[start+sindex],y[start+sindex]]
j = [x[dest+eindex],y[dest+eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Sanne',euc(i,j))

# +
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':');

def euc(a,b):
    return distance.euclidean(a,b)
bird_names = pd.unique(bird.bird_name)

sindex = 15000
eindex = 18300

ix = bird['bird_name'] == 'Eric'
x,y = bird.longitude[ix], bird.latitude[ix]

i = [x[sindex],y[sindex]]
j = [x[eindex],y[eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Eric',euc(i,j))

ix = bird['bird_name'] == 'Nico'
x,y = bird.longitude[ix], bird.latitude[ix]
start = len(x)
dest = len(y)

i = [x[start+sindex],y[start+sindex]]
j = [x[dest+eindex],y[dest+eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Nico',euc(i,j))

ix = bird['bird_name'] == 'Sanne'
x,y = bird.longitude[ix], bird.latitude[ix]
start = start+len(x)
dest = dest+len(x)

i = [x[start+sindex],y[start+sindex]]
j = [x[dest+eindex],y[dest+eindex]]
ax.plot(x[sindex:eindex],y[sindex:eindex],'.', transform=ccrs.Geodetic());                
print('Sanne',euc(i,j))
# -

longest = 0
distlist = []
def euc(a,b):
    return distance.euclidean(a,b)
ix = bird['bird_name'] == 'Eric'
x,y = bird.longitude[ix], bird.latitude[ix]
i = [x[0],y[0]]
for ind in range(len(x)-1):
    j = [x[ind+1], y[ind+1]]
    newlength = euc(i,j)
    distlist.append(newlength)
    if (euc(i,j)>longest):
        longest = newlength
print('Longest=',longest)

# +
bird_names = pd.unique(bird.bird_name)
bird_dist = {}

def euc(a,b):
    return distance.euclidean(a,b)

start = 0
end = 0
count = 0
for bird_name in bird_names:
    ix = bird['bird_name'] == bird_name
    x, y = bird.longitude[ix], bird.latitude[ix]
    longest = 0
    i = [x[start], y[start]]
    
    for ind in range(len(x)-1):
        j = [x[start+ind+1], y[start+ind+1]]
        newlength = euc(i,j)
        distlist.append(newlength)
        if(euc(i,j)>longest):
            longest = newlength
            
    bird_dist[bird_names[count]] = longest
    count = count+1
    start = start+len(x)
    dest = dest+len(x)

print(bird_dist)
# -

new_dict = {"bird":['Eric','Nico','Sanne'],"dist":[22.59911272537230,43.44920181082738,40.87144067458034]}
bird_frame = pd.DataFrame(new_dict)
print(bird_frame)
