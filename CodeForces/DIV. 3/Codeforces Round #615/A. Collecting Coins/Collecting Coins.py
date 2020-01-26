t=int(input())
while t:
    a,b,c,n=map(int,input().split())
    m=max(a,b,c)
    rem=((a+b+c+n)-(3*m))
    if rem%3==0 and rem>=0:
        print("YES")
    else:
        print("NO")
    t-=1

