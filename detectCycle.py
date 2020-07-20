"""
Pandu is interested in solving problems on Graph data structure and while he is solving those problems he noticed a problem statement as follows:

Given a directed graph with V vertices and E edges. You need to detect whether the graph contains any cycle formation of vertices or not.

If it is cyclic graph print "yes" else print "no"

Input:

First line consists of V vertices and E edges

Next E lines consists of edges connecting two  vertices

Output:

print whether the contains cycle or not

Example 1:

Input:
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5

Output:
no

Example 2:

Input:
4 5
1 2
2 3
3 4
4 3
3 1

Output:
yes

"""

def addEdge(s,d,graph):
    graph[s].append(d)
def detectCycle(v,s,visit):
    visit[v]=True
    s[v]=True
    for i in range(len(graph[v])):
        if visit[graph[v][i]]==False:
            if detectCycle(graph[v][i],s,visit):
                return True
        else:
            return True
    s[v]=False
    return False
v,e=map(int,input().split())
graph=[[]for i in range(v+1)]
visit=[False]*(v+1)
stack=[False]*(v+1)
for i in range(e):
    s,d=map(int,input().split())
    addEdge(s,d,graph)
flag=False
for i in range(1,len(graph)):
    if visit[i]==False:
        if detectCycle(i,stack,visit)==True:
            flag=True
        break
if flag:
    print("yes")
else:
    print("no")
    
