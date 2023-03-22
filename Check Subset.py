testcases = int(input()) 
for i in range(testcases):
    no_of_elements_a = int(input()) 
    a = set(map(int, input().split()))
    no_of_elements_b = int(input()) 
    b = set(map(int, input().split())) 
    b.intersection_update(a)
    if a == b:
        print(True) 
    else:
        print(False)