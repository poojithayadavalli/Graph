"""
Kohli  is learning Graph Theory and he is given a task to solve on Graphs.The task is given below:

Given a directed graph with V vertices, E edges and a source vertex S and all edges in the graph.

The task is to find the all the vertices that can be reached from  the given source vertex.If no vertex exist print -1

Input:

Firstline contains number of edges V
Secondline contains source vertex S
Third line contains number of edges E
Next E lines Contains edges connecting two vertices

Output:

print all the reachable vertices from the given vertex in sorted order

Example 1:

Input:
5
1
8
1 2
2 3
2 4
1 3
1 4
3 4
2 5
4 5

Output:
2 3 4 5

Example 2:

Input:
4
3
5
1 2
3 2
3 4
2 4
1 4

Output:
2 4
"""

graph = [[] for _ in range(100000)] 

def addEdge(S, D):
    graph[S].append(D)

def reachable(S, V ):
    node=[]
    q=[]
    q.append(S)
    if (len(graph[S]) > 0):
        while len(q)>0:
            x=q.pop(0)
            for i in range(len(graph[x])):
                if graph[x][i] not in node:
                    node.append(graph[x][i])
                    q.append(graph[x][i])
        return node
    else:
        return [-1]
v = int(input())
S = int(input())
e = int(input())
for i in range(e):
    x,y = map(int,input().split())
    addEdge(x,y)
y=sorted(reachable(S,v))
print(*y)
