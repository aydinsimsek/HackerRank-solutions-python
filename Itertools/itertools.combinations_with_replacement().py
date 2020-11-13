from itertools import combinations_with_replacement

S, k = input().split(" ") 
s = list(S)
s.sort()
com = list(combinations_with_replacement(s, int(k))) 
for i in com: 
    print("".join(i))  
