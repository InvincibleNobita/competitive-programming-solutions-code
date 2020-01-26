
#code for dynamo

t = int(input())
while t:
    n = int(input())
    p = 10**n
    a = int(input())
    print(a+(2*p))
    b = int(input())
    print(p-b)
    d = int(input())
    print(p-d)
    res = int(input())
    if (res!=1):
        break
    t -= 1
