n = int(input())
s = set(map(int, input().split()))
N = int(input())
sum = 0 

for cmd in range(N): 
    cmd = input().split()
    if (cmd[0] == "remove"): 
        s.remove(int(cmd[1]))
    elif (cmd[0] == "discard"):
        s.discard(int(cmd[1]))
    elif (cmd[0] == "pop"):
        s.pop()

for item in s: 
    sum += item 
print(sum) 
