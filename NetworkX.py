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
