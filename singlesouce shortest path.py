"""
Sachin  is learning Graph Theory and he is given a task to solve on Graphs.The task is given below:

Given a directed weighted graph with V vertices, E edges and a source vertex S and all edges in the graph.

The task is to find the nearest neighbouring node to the given source vertex.If mutliple nodes exist print first node in order and if no node exist print -1

Note:Nearest neighbour is a neighbour with least weight

Input:

Firstline contains number of edges V
Secondline contains source and destination vertices S ,D
Third line contains number of edges E
Next E lines Contains edges connecting two vertices and its weight

Output:

print the shortest path length from source vertex to destination vertex

Example 1:
Input:
5
1
8
1 2 1
2 3 7
2 4 -2
1 3 8
1 4 9
3 4 3 
2 5 3 
4 5 -3

Output:
5

Example 2:

Input:
4
3
5
1 2 2
3 2 1
3 4 5
2 4 1
1 4 3

Output:
2
"""

graph = [[] for _ in range(100000)] 

def addEdge(S, D, weight):
    graph[S].append([D, weight])

def nearestNeighbour(S, V ):
    d = [10**9]*(V + 1)
    d[S] = 0
    weight=10**10
    if (graph[S] > 0):
        for i in range(len(graph[S])):
            if graph[S][i][1]<weight:
                weight=graph[S][i][1]
                node=graph[S][i][0]
            elif graph[S][i][1]==weight:
                node=min(graph[S][i][0],node)
        return node
    else:
        return -1
v=int(input())
S,D=map(int,input().split())
e=int(input())
for i in range(e):
    x,y,z=map(int,input().split())
    addEdge(x,y,z)
print(shortestPath(S,D,v))
