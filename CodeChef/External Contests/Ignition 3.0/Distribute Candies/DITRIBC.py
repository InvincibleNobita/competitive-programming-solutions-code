
#ignition distribute
t = int(input())
while t:
    n = int(input())
    cl = []
    i = 0
    while i<n:
        a,c = map(int, input().split())
        cl.append(c)
        i+=1
    rem = n % sum(cl)
    if rem == n:
        rem = sum(cl)-n
    print(rem)
    t -= 1

