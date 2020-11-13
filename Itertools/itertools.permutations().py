from itertools import permutations

S, k = input().split(" ")
s = list(S)
s.sort()
per = list(permutations(s, int (k))) 
for i in per: 
    print("".join(i))  
