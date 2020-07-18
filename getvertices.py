"""
Problem Description

You are given some routes connecting two places.Your task is to connect all the routes given in the form of a graph.

Input:
First line consists of no of places V
second line consists of no of routes U
next U line conists of routes connecting two places x and y

Output:
print all the graph formed by connecting all the routes (use dfs to represent graph)


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
0 4 1 2 3


"""


import queue
def addEdge(adj, u, v): 
    adj[u].append(v)

def bfsUtil(u, adj, visited):
    q = queue.Queue()
    visited[u] = True
    q.put(u)
    
    while(not q.empty()): 
        u = q.queue[0]  
        print(u, end = " ")  
        q.get() 
        i = 0
        while i != len(adj[u]):
            if(not visited[adj[u][i]]):
                visited[adj[u][i]] = True
                q.put(adj[u][i])
            i += 1 
def BFS(adj, V): 
    visited = [False] * V  
    for u in range(V): 
        if (visited[u] == False):  
            bfsUtil(u, adj, visited) 
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
BFS(adj,v)
