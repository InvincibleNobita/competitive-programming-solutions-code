t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    g = n//4
    p,q,r,s = l[:g],l[g:2*g],l[2*g:3*g],l[3*g:]
    x,y,z = q[0],r[0],s[0]
    if x == p[-1] or y == q[-1] or z == r[-1]:
        print(-1)
    else:
        print(x,y,z,sep=' ')
    t -= 1
