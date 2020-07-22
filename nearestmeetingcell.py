"""

You are given a directed graph with N vertices.Each vertex of the given graph can have multiple incoming edges but it must have a single outgoing edge.

If the vertex doesnt have an outgoing edge then it is indicated with -1.Two vertices v1 and v2 are given in which the task is to find 

the nearest meeting vertex of both vertices.(The nearest vertex that have path from both v1 and v2).If no such vertex exists print -1

Input:

Firstline consists of number of vertices v
Secondline has an edge array in which vertex i points to vertex edge[i]
Nextline contains two vertices v1 and v2

Output:

print the nearest meeting vertex from v1 and v2

Example 1:

Input:

5
1 -1 1 2 3
0 2

Output:

1

Example 2:

Input:

4
2 -1 3 -1
2 3

Output:
 
 3

"""
def  addEdge(s,d,g):
    g[s]=d
def Dfsutil(g,c1,visited):
    visited[c1]=True
    while g[c1]!=-1 and g[c1]!=True:
        c1=g[c1]
        visited[c1]=True
    
def nearestMeeting(g,c1,c2):
    visited=[False]*len(g)
    Dfsutil(g,c1,visited)
    
    if visited[c2]==True:
        return c2
    while g[c2]!=-1 and g[c2]!=True:
        c2=g[c2]
        if visited[c2]==True:
            return c2
    return -1
        

v=int(input())
g=[-1]*v
e=list(map(int,input().split()))
for i in range(len(e)):
    addEdge(i,e[i],g)
c1,c2=map(int,input().split())
print(nearestMeeting(g,c1,c2))
