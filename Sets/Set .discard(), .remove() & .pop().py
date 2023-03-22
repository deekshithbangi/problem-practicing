n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    temp = input().split()
    if len(temp) == 1:
        s.pop() 
    elif len(temp) == 2:
        operation = temp[0] 
        value = int(temp[1])
        if operation == 'remove':
            s.remove(value) 
        elif operation == 'discard':
            s.discard(value) 
print(sum(s))