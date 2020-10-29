T = int(input()) 
for _ in range(T): 
    a = int(input())
    A = set(map(int, input().split())) 
    b = int(input())
    B = set(map(int, input().split())) 
    if(A.difference(B) == set()):
        print("True")
    else: 
        print("False")
