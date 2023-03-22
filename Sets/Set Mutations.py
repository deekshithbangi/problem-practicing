n , a = int(input()), set(map(int, input().split())) 

for i in range(int(input())):
    operation = input().split()
    values = set(map(int, input().split()))
    
    if 'intersection_update' == operation[0]:
        a.intersection_update(values)

    elif 'difference_update' == operation[0]:
        a.difference_update(values)
        
    elif 'symmetric_difference_update' == operation[0]:
        a.symmetric_difference_update(values)
        
    elif 'update' in operation[0]:
        a.update(values) 

print(sum(a))
