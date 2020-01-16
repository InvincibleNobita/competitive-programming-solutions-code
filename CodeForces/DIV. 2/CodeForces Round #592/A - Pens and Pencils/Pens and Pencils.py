from math import ceil

t = int(input())
while t:
    a,b,c,d,k = map(int, input().split())
    tp = ceil(a/c)
    tcil = ceil(b/d)
    te = tp + tcil
    if te <= k:
        print(tp,tcil,sep=' ')
    else:
        print(-1)
    t -= 1
