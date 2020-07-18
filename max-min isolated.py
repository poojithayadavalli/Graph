"""

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
