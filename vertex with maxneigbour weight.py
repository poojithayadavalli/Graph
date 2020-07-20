"""
Raja used to spend time with her neighbours.Since she is very friendly all famous neighbours like to spend time with her.she is awarded as

Popular neighbour by their neighbours.Now the task is to find the Popular neighbour in the undirected graph.Given a graph with V vertices and E edges.Find the Vertex 

that has largest sum of weights of neighbours.If many best neighbours exist print the first Vertex in the order.

Input:

Firstline contains number of vertices V
Second line consists of number of edges E
Next E lines contains the edges connecting two vertices and its weight

Output:

print the Popular neighbour

Example 1:

Input:

6
5
1 2 3
2 6 6
2 5 5
2 4 4
3 4 2

Output:
2

Example 2:

Input:
5
4
1 2 3
1 4 6
1 4 10
3 2 20

Output:
2
"""
def addEdge(s,d,graph,weight):
    graph[s].append([d,weight])
    graph[d].append([s,weight])
def popularNeighbour(graph):
    l=-10000
    for i in range(1,len(graph)):
        sum1=0
        if len(graph[i])>0:
            for j in range(len(graph[i])):
                sum1+=graph[i][j][1]
        if sum1>l:
            l=sum1
            best=i
    return best
v=int(input())
e=int(input())
g=[[]for i in range(v+1)]
for i in range(e):
    s,d,w=map(int,input().split())
    addEdge(s,d,g,w)
print(popularNeighbour(g))
