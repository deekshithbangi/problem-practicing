from itertools import combinations 

temp = input().split() 
s = ''.join(sorted(temp[0]))
r = int(temp[1])

for i in range(1,r+1):
    ans = (list(combinations(s,i))) 
    for j in ans:
        print(''.join(j))