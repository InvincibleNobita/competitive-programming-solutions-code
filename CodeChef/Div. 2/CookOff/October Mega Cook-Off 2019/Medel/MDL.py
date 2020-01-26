#from collections import deque

t = int(input())
while t:
    n = int(input())
    #d = deque(map(int, input().split()))
    l = list(map(int, input().split()))
    a = []
    maxi = max(l)
    mini = min(l)
    if l.index(maxi) > l.index(mini):
        a.append(mini)
        a.append(maxi)
    else:
        a.append(maxi)
        a.append(mini)
    print(*a,sep=' ')        
    t -= 1
