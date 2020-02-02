t = int(input())
while t:
    n = int(input())
    c = int(input())
    count = 1
    a,b = 1,1
    while a<=n:
        if a != 1:
            count += 1
        a,b=b,a+b
    print(count*c)
    t -= 1
