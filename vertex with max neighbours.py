"""

Kavitha is a student and she used to spend time with her neighbours.Since she is very friendly all of her neighbours like to spend time with her.she is awarded as

Best neighbour by their neighbours.Now the task is to find the best neighbour in the undirected graph.Given a graph with V vertices and E edges.Find the Vertex 

that has more number of neighbours.If many best neighbours exist print the first Vertex in the order.

Input:

Firstline contains number of vertices V
Second line consists of number of edges E
Next E lines contains the edges connecting two vertices

Output:
print the Best Neighbour

Example 1:

Input:
4
3
1 2
2 3
3 4

Output:
2

Example 2:

Input:
5
4
1 2
1 3
2 3
2 4

Output:
2

"""
def addEdge(s,d,graph):
    graph[s].append(d)
    graph[d].append(s)
def bestNeighbour(graph):
    l=0
    for i in range(1,len(graph)):
        if len(graph[i])>l:
            l=len(graph[i])
            best=i
    return best
v=int(input())
e=int(input())
g=[[]for i in range(v+1)]
for i in range(e):
    s,d=map(int,input().split())
    addEdge(s,d,g)
print(bestNeighbour(g))

