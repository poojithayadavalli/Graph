"""
"""
def  addEdge(s,d,g):
    g[s]=d
def Dfsutil(g,c1,visited):
    visited[c1]=True
    while g[c1]!=-1:
        c1=g[c1]
        visited[c1]=True
    
def nearestMeeting(g,c1,c2):
    visited=[False]*len(g)
    Dfsutil(g,c1,visited)
    
    if visited[c2]==True:
        return c2
    while g[c2]!=-1:
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
