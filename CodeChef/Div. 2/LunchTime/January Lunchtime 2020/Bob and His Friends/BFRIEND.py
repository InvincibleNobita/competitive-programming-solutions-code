t=int(input())
while t:
    n,a,b,c=map(int,input().split())
    ff=list(map(int,input().split()))
    mint=abs(max(ff)-b)+abs(max(ff)-a)+c
    for item in ff:
        if a<=item<=b or b<=item<=a:
            mint=abs(item-a)+abs(item-b)
            break
        else:
            bd=abs(item-b)
            da=abs(item-a)
            time=bd+da
            if time<mint:
                mint=time
    print(mint+c)     
    t-=1
