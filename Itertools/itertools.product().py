from itertools import product 
a = list(map(int, input().split() ))
b = list(map(int, input().split() )) 
ans = product(a,b,repeat=1)
print(*ans)
