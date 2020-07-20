"""
Chitra is learning about directed graphs and she went through a task as follows:

Given directed graph with 𝑛 vertices and 𝑚 edges.The task is to find the number of strongly connected components in the graph.

A directed graph is said to be strongly connected if there is a path between all pairs of vertices.

Input:

Firstline consists of number of vertices n and number of edges m
Next m lines consist of edges connecting two vertices

Output:

Print the number of Strongly connected components

Example 1:

Input:
4 4
1 2
4 1
2 3
3 1

Output:
2

Example 2:

Input:
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3

Output:
5
"""

def dfs(adj,x,visited,stack):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            dfs(adj,i,visited,stack)
    stack.append(x)

def reverseEdges(adj):
    rev_adj = [[] for _ in range(len(adj))]
    for i in range(1,len(adj)):
        for j in range(len(adj[i])):
            rev_adj[adj[i][j]].append(i)
    return rev_adj


def scc(adj):
    result = 0
    stack = []
    visited = [False] * len(adj)

    for i in range(1,len(adj)):
        if not visited[i]:
            dfs(adj,i,visited,stack)

    rev_adj = reverseEdges(adj)
    visited = [False]*len(adj)

    while stack:
        x = stack.pop()
        if not visited[x]:
            dfs(rev_adj,x,visited,[])
            result += 1
    return result

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
print(scc(adj))
