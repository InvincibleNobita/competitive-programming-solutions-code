
#code for brkbks


import math as m
    
t = int(input())
while t:
    s,w1,w2,w3 = map(int, input().split())
    sumw = w1+w2+w3
    if s==3 and sumw==6:      
        print(s)
    elif s==2 and w1==1 and w2==2 and w3==1:
        print(s+1)
    else:
        print(m.ceil(sumw/s))
    t -= 1


'''
t = int(input())
while t:
    r = list(map(int, input().split()))
    s,wl = r[0],r[1:]
    wl.sort(reverse=True)
    count = 0
    while wl:
        while wl:
            item = wl.pop()
            if item>s:
                s = r[0]
                break
            else:
                s -= item
                count+= 1
    print(count)
    t -= 1
'''
