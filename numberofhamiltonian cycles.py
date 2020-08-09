"""

Koushik is leaning about hamiltonian cycle and he saw a task as follows:

Given an undirected complete graph of N vertices where N > 2. The task is to find the number of different Hamiltonian cycle of the graph.

A graph is said to be complete if each possible vertices is connected through an Edge and Hamiltonian Cycle

is a closed path such that each vertex is visited at most once except the initial vertex. and it is not necessary to visit all the edges.

Input:

Input consists of number of vertices of a graph N

Output:

Print the number of hamiltonian cycles possible in the graph

Example:

Input:

6

Output:

120

Example 2:

Input:

5

Output:

12

"""

def Cycles(N):
    if N==0:
        return 0
    fact = 1
    result = N - 1
    i = result 
    while (i > 0): 
        fact = fact * i 
        i -= 1 
    return fact
N = int(input())
Number = Cycles(N)
