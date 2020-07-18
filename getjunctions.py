"""

"""

def addEdge(adj, u, v): 
    adj[u].append(v)

def junction(adj):
    l=[]
    for i in range(len(adj)):
        if len(adj[i])>1:
            l.append(str(i))
    return " ".join(l)
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
print(junction(adj))
