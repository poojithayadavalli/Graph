"""

Ram is fond of Graph theory and he came across a task as follows:

A disconnected undirectional Graph with N vertices and K edges is given. The task is to find the count of singleton sub-graphs. 

A singleton graph is one with only single vertex.

Input:

First line contains no of vertices N
Second line contains no of edges K
Next K lines contains edges between two vertices

Output:

print all the singleton sub graphs


Example:

Input:

6
3
1 2
1 3
5 6

Output:

4

Explanation:

we have three connected subgraphs 1-2-3, 5-6 , 4.since 4 is only node in that sub graph it is the answer.

Example 2:

Input:

6
4
1 2
2 3
1 4
2 4

Output:

5 6

"""
def addEdge(adj, u, v): 
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

def singleton(adj):
    l=[]
    for i in range(len(adj)):
        if adj[i]==[]:
            l.append(str(i+1))
    return " ".join(l)
  
v=int(input())
u=int(input())
adj = [[] for i in range(v)]
for i in range(u):
    x,y=map(int,input().split())
    addEdge(adj,x,y)
print(singleton(adj))
