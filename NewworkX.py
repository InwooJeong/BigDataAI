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
