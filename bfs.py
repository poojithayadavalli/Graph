"""
Given a directed graph with V vertices and E edges.Vijay wants to traverse the graph using breadth first traversal so he need your help.

Input:

First line consists of number of vertices V and number of edges E
Next E lines contains edges connecting two vertices

Output:
print the vertices of graphs using BFS

Example 1:

Input:

4 3
1 2
1 3
2 3

Output:

1 2 3 4

Example 2:

Input:

5 3
1 2
1 3
2 5

Output:

1 2 3 5 4

"""

def addEdge(s,d,graph):
    graph[s].append(d)
def bfs(graph,visit):
    l=[]
    for i in range(1,len(graph)):
        if visit[i]==False:
            visit[i]=True
            q=[]
            q.append(i)
            while q:
                u=q.pop(0)
                l.append(str(u))
                for j in range(len(graph[u])):
                    if visit[graph[u][j]]==False:
                        q.append(graph[u][j])
                        visit[graph[u][j]]=True
    return " ".join(l)

v,e=map(int,input().split())
g=[[]for i in range(v+1)]
visit=[False]*(v+1)
for i in range(e):
    s,d=map(int,input().split())
    addEdge(s,d,g)
print(bfs(g,visit))
        
