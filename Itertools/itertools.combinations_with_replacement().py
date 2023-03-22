from itertools import combinations_with_replacement 

temp = input().split() 
s = ''.join(sorted(temp[0]))
r = int(temp[1])

ans = list(combinations_with_replacement(s,r) ) 
for j in ans:
    print(''.join(j))