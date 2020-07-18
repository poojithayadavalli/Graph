"""
Problem Description

You are given some routes connecting two places.Your task is to connect all the routes given in the form of a graph.
and find all the junctions in the graph

Input:

First line consists of no of places V
second line consists of no of routes U
next U line conists of routes connecting two places x and y

Output:

print all the junction nodes in the graph

Example:

Input:

5
6
0 4
1 2
1 3
1 4
2 3
3 4

Output:

1

"""

def addEdge(adj, u, v): 
    adj[u].append(v)

def junction(adj):
    l=[]
    for i in range(len(adj)):
        if len(adj[i])>1:
            l.append(str(i))
    return " ".join(l)
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
print(junction(adj))
