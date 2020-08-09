"""
Maximum Weight Cell
Given a maze with N cells. A Maze is similar to a directed graph.Each cell may have multiple entry paths but it must have only one exit path.

The cells are numbered from 0 to N.Your task is to find the maximum weight cell in the maze.Weight of a cell is the sum of all node numbers pointing to it.

If a cell doesnt have an exit then exit is indicated as -1.

Input:

First line contains integer N denoting the number of cells
Second line contains Edge array in which cell i points to the cell Edge[i]

Output:

print the maximum weight cell.

Example:

Input:

5
2 3 4 4 4

Output:
4

Example 2:

Input:

4
2 2 -1 1

Output:

1

"""
def  addEdge(s,d,g,w):
    g[s].append(d)
    if d!=-1:
      w[d]+=s
    
def maxWeightnode(w):
    return w.index(max(w))

v=int(input())
g=[[]for i in range(v)]
w=[0]*(v)
e=list(map(int,input().split()))
for i in range(len(e)):
    addEdge(i,e[i],g,w)
    
print(maxWeightnode(w))

