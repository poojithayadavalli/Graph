"""
Rajesh is working with graphs and he notices a task based on isolated vertices as follows:

Given ‘n’ vertices and ‘m’ edges of a graph. Find the minimum number and maximum number of isolated vertices that are possible in the graph.

Input:

The First line consists of no of vertices n
Second line consists of no of Edges

Output:

print the minimum and maximum possible isolated vertices 


Example 1:

Input:

4
2

Output:

0 1

Example 2:

Input:

 5
 2
 
 Output:
 
 1 2

"""
def findsol(n, m) :  
    if (n <= 2 * m): 
        mini = 0  
    else: 
        min = n - 2 * m
        
    for i in range(1, n + 1):  
        if (i * (i - 1) // 2 >= m):  
            break
    maxi = n - i
return maxi, mini

n,m=map(int,input().split())
x,y=findsol(n,m)

print(x,y,sep=" ")
