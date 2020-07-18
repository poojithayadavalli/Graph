"""

Ram is fond of Graph theory and he came across a task as follows:

A disconnected undirectional Graph with N vertices and K edges is given. The task is to find the count of singleton sub-graphs. 

A singleton graph is one with only single vertex.

Input:

First line contains no of vertices N
Second line contains no of edges K
Next K lines contains edges between two vertices

Output:

print all the singleton sub graphs


Example:

Input:

6
3
1 2
1 3
5 6

Output:

4

"""
def addEdge(adj, u, v): 
    adj[u].append(v)
    adj[v].append(u)

def singleton(adj):
    l=[]
    for i in range(len(adj)):
        if len(adj[i])==None:
            l.append(str(i))
    return " ".join(l)
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
print(singleton(adj))
