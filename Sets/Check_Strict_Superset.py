A = set(map(int, input().split())) 
n = int(input())
result = "True"
for _ in range(n): 
    N = set(map(int, input().split())) 
    if (N.difference(A) != set()):
        result = "False"  
        break
print(result) 
