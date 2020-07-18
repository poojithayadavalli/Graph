"""
Given a connected graph with N vertices. The task is to select k vertices from the graph such that all these selected vertices are connected to at least one of the non selected vertex. 

In case of multiple answers print any one of them.

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

1 3  ({1,2}{1,4},{2,3}{2,4}{3,4} are also possible)

Example 2:

Input:

3 2
1 2
1 3

output:

1 ({2},{3} are also possible)

"""

