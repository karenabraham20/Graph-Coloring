import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Graph():  

    def __init__(self, n): 
        self.V = n 
        self.graph = [[0 for column in range(n)]for row in range(n)] 

    def isSafe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    def graphColourUtil(self, n, colour, v): 
        if v == self.V: 
            return True

        for c in range(1, n + 1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(n, colour, v + 1) == True: 
                    return True
                colour[v] = 0  

    def graphColouring(self, n): 
        colour = [0] * self.V
        if self.graphColourUtil(n, colour, 0) == None: 
            return False  

        print("Chromatic Number of the given graph:")
        print(len(set(colour)))

        return colour

  
n=int(input("Enter the number of vertices: "))
g = Graph(n) 
a=[]
for i in range(0,n):
    a.append(list(map(int,input().split())))
print(a)

g.graph=a

colour=g.graphColouring(n) 
G = nx.Graph()
G=nx.from_numpy_matrix(np.array(a))

vmap={}
vmap={1:1.0,2:0.5714285714285714,3: 0.0}
val_map={}
t=0

for i in colour:
    if i in vmap:
       val_map[t]=vmap[i]
       t+=1
       if(t==len(colour)):
           break 

values = [val_map.get(node, 0.25) for node in G.nodes()]

nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')

plt.show()
