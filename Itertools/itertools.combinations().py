from itertools import combinations

S, k = input().split(" ") 
s = list(S) 
s.sort()
for i in range(1, int(k)+1):   
    for com in combinations(s, int(i)): 
        print("".join(com))  
