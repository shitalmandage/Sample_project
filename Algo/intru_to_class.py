class Graph():
    def __init__(self,vertices,edges):
        self.graph=defaultdict(list)
        self.v=vertices
        self.e=edges
        print(self.v,self.e)
    def addEdge(self,u,v):
        self.graph[u].append(v)

import sys
from collections import defaultdict
g=Graph(4,3)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.graph)
