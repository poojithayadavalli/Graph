"""
Harry Potter is learning Graph Theory and he is given a task to solve on Graphs.The task is given below:

Given a directed weighted graph with V vertices, E edges and a source vertex S and destination vertex D. 

The task is to find the shortest path from the source vertex to the destination vertex.

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
1 4
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

-1

Example 2:
Input:

4
3 4
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

def shortestPath(S, D, V ):
    d = [10**9]*(V + 1) 
    inQueue = [False]*(V + 1)
    d[S] = 0
    q = [] 
    q.append(S) 
    inQueue[S] = True
  
    while (len(q) > 0):
        u = q.pop(0) 
        inQueue[u] = False
        for i in range(len(graph[u])):
            v = graph[u][i][0] 
            weight = graph[u][i][1]
  
            if (d[v] > d[u] + weight):
                d[v] = d[u] + weight
                if (inQueue[v] == False):
                    q.append(v) 
                    inQueue[v] = True

    return d[D]
v=int(input())
S,D=map(int,input().split())
e=int(input())
for i in range(e):
    x,y,z=map(int,input().split())
    addEdge(x,y,z)
print(shortestPath(S,D,v))  
