a = set(map(int, input().split())) 
no_of_sets = int(input()) 
c = 0
for i in range(no_of_sets):
    otherSet = set(map(int, input().split())) 
    temp = a.intersection(otherSet) 
    if len(temp) == len(otherSet):
        c +=1
if c == no_of_sets:
    print(True)
else:
    print(False)