from itertools import permutations
temp = input().split() 
s = ''.join(sorted(temp[0]))

permutations_list = list(permutations(s, int(temp[1]) )) 
for i in permutations_list:
    print(''.join(i))