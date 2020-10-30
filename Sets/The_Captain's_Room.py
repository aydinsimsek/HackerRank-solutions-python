K = int(input())
R = input().split()  
S1 = set()
S2 = set() 
for i in range(len(R)): 
    if R[i] in S1: 
        S2.add(R[i])
    else: 
        S1.add(R[i])  
print(S1.difference(S2).pop())   
