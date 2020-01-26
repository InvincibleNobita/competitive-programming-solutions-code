def series(n):
    a1,a2 = 0,0
    cl=[a1,a2]
    while len(cl)<n:
        x = cl[-1]
        if x not in cl[:-1]:
            cl.append(0)
        else:
            t = cl[:-1]
            t.reverse()
            pos = t.index(x)
            rpos = len(t)-pos-1
            cl.append(len(cl)-rpos-1)
    return cl
T = int(input())
while T:
    N = int(input())
    l = series(N)
    y,count = l[-1],1
    for i in range(0,N-1):
        if l[i] == y:
            count += 1
    print(count)
    T -= 1
