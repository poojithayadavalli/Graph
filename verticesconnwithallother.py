"""
You are given n vertices and m edges of a graph.your task is to find all the vertices that are connected with the remaining all other vertices in the graph.

If no such vertices are present in the graph print -1

Note :given graph is undirected graph

Input:

First line contains number of vertices n
Second line contains number of edged m
Next m lines contains edges connecting two vertices a and b

Output:

all vertices that satisfies given condition

Example 1:

Input:

5
3
1 3
1 4
1 5

Output:

-1

Example 2:

Input:

6
5
1 2
1 3
1 4
1 5
1 6

Output:

1

Example 3:

Input:

4
6
1 2
1 3
2 3
2 4
1 4
3 4

Output:

1 2 3

"""
def addEdge(adj, u, v): 
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

def allconnected(adj):
    s=[]
    for i in range(len(adj)):
        l=[j for j in range(len(adj))if j!=i]
        if l==sorted(adj[i]):
            s.append(str(i+1))
    if len(s)==0:
        s=["-1"]
    return " ".join(s)
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
print(allconnected(adj) if u>=v-1 else "-1")
