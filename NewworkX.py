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

import networkx as nx
G = nx.Graph()

G.add_node(1)
print(G.nodes())

G.add_node('P')
G.add_node('Hi')
print(G.nodes())

G.add_nodes_from([2,3])
print(G.nodes)

for i in G.nodes:
    print(i)

G.add_nodes_from([3,4])
print(G.nodes)

nx.draw(G, with_labels=True,node_color='lightblue')

G.add_edge(1,2)
nx.draw(G,with_labels=True,node_color='lightblue',edge_color='grey')

print(G.edges())

G.add_edge(4,5)
print(G.edges())

G.add_edges_from([(1,2),(1,3),(1,4),(1,5)])
print(G.edges())

G.add_edges_from([(1,'P'),(1,'Hi')])
nx.draw(G,with_labels=True,node_color='yellow',edge_color='red')

G = nx.path_graph(4)
nx.draw(G,with_labels=True,node_color='lightblue',edge_color='grey')

G = nx.Graph()
nx.add_path(G,[0,1,2,3])
nx.draw(G,with_labels=True,node_color='lightblue',edge_color='grey')

G = nx.Graph()
nx.add_path(G,[0,1,2,3])
print(G.degree(0))  # 노드 0에 대한 차수
print(G.degree([0,1]))  # 노드 0과 1에 대한 차수만 출력
print(G.degree())  # 모든 노드에 대한 차수 출력

print(G.edges())
G.remove_edge(1,2)
print(G.edges())

print(G.edges())
G.remove_edges_from([(0,1),(2,3)])
print(G.edges())

print(G.nodes())
G.remove_node(2)
print(G.nodes())

print(G.nodes())
G.remove_nodes_from([0,1,3])
print(G.nodes())

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5)])
print('No. nodes:',G.number_of_nodes())
print('No. edges:',G.number_of_edges())

G.remove_edge(1,3)
print('No. nodes:',G.number_of_nodes())
print('No. edges:',G.number_of_edges())

# +
G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5)])
G.remove_node(3)

print('No. nodes:',G.number_of_nodes())
print('No. edges:',G.number_of_edges())

# +
G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5)])
G.remove_node(4)

print('No. nodes:',G.number_of_nodes())
print('No. edges:',G.number_of_edges())

# +
G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5)])
G.remove_nodes_from([4,5])

print('No. nodes:',G.number_of_nodes())
print('No. edges:',G.number_of_edges())
# -

# ## 특정 확률분포 그래프 생성기
#
# - 다양한 확률분포 모델에 의해 그래프를 생성할 수 있음
# - 노드 개수와 노드 간 연결 확률(N,p)

import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(25,0.2)
nx.draw(G)

G = nx.watts_strogatz_graph(30,3,0.1)
nx.draw(G)

G = nx.barabasi_albert_graph(25,5)
nx.draw(G)

from scipy.stats import bernoulli
for i in range(6):
    print(bernoulli.rvs(p=0.33))

# +
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def erdosGraph(N,p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    listG = list(G.nodes())
    for i, node1 in enumerate(listG):
        for node2 in listG[i+1:]:
            # print(listG[i+1:])
            if(bernoulli.rvs(p=p)):
                G.add_edge(node1,node2)
    return G


# -

nx.draw(erdosGraph(20,0.18))

G1 = erdosGraph(80,0.3)
plt.hist(list([d for n, d in G1.degree()]),histtype='step')


# +
def pltGraph(G):
    plt.hist(list([d for n, d in G.degree()]),histtype='step')
    
G1 = erdosGraph(80,0.3)
pltGraph(G1)
G2 = erdosGraph(80,0.3)
pltGraph(G2)
G3 = erdosGraph(80,0.3)
pltGraph(G3)
# -

import numpy as np
import networkx as nx
K = np.loadtxt("test1.csv",delimiter=",",encoding="UTF-8-SIG")
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

import chardet
with open('test1.csv', 'rb') as f:
    result = chardet.detect(f.readline())  # or read() if the file is small.
    print(result['encoding'])

K = np.loadtxt("test2.csv",delimiter=",",encoding="UTF-8-SIG")
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')
