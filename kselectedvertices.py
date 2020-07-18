"""
Given a connected graph with N vertices. The task is to select k vertices from the graph such that all these selected vertices are connected to at least one of the non selected vertex. 

There are mutltiple combinations of possible answers print any one of them(preferably first possible combination).

Note: The graph is always a complete graph

Input:

Firstline consists of numbers of vertices n and number of edges m
next m lines contains the edges connecting two  vertices

Output:

print any such combination of vertices

Example1:

Input:

4 6
1 2
1 3
1 4
1 3
2 4

Output

2 4  ({1,2}{1,4},{2,3}{1,3}{3,4} are also possible)

Example 2:

Input:

3 3
1 2
1 3
2 3

output:

2 ({1},{3} are also possible)

"""
n,m=map(int,input().split())
vis=[0 for i in range(n)] 
gr=[[] for i in range(n)] 
v=[[] for i in range(2)]
def add_edges(x, y): 
    gr[x].append(y) 
    gr[y].append(x) 
  
def dfs(x, state):
    v[state].append(x+1)
    vis[x] = 1
    for i in gr[x]: 
        if (vis[i] == 0): 
            dfs(i, state ^ 1) 
def Print_vertices():
    if (len(v[0]) <= len(v[1])): 
        for i in v[0]: 
            print(i,end=" ") 
    else: 
        for i in v[1]: 
            print(i,end=" ") 
  

for i in range(m):
    x,y=map(int,input().split())
    add_edges(x-1, y-1)
dfs(0, 0)
Print_vertices() 

