M = int(input())
A = set(map(int, input().split())) 
N = int(input()) 

for _ in range(N): 
    op, l = input().split()
    B = set(map(int, input().split()))   
    if(op == "update"): 
        A.update(B)
    elif(op == "intersection_update"): 
        A.intersection_update(B)
    elif(op == "difference_update"): 
        A.difference_update(B)
    elif(op == "symmetric_difference_update"): 
        A.symmetric_difference_update(B) 

print(sum(A))   
