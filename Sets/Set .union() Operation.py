n, english = int(input()) , set(map(int, input().split())) 
m, french = int(input()) , set(map(int, input().split()))  
print(len(english.union(french)))