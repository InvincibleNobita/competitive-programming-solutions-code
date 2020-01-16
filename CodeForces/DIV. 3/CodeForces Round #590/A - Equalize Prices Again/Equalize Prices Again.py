import math as m                 

q = int(input())
i = 0
while i < q:
    n = int(input())
    l = list(map(int, input().split()))
    val = m.ceil(sum(l)/len(l))
    print(val)
    i += 1
