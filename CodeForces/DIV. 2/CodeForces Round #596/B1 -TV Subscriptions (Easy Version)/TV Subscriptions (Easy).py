t = int(input())
while t:
    n,k,d = map(int, input().split())
    l = list(map(int, input().split()))
    mini = len(l)
    for i in range(0,len(l)-(d-1)):
        n = []
        for j in range(i,i+d):
            if l[j] not in n:
                n.append(l[j])
        if mini > len(n):
            mini = len(n)
    print(mini)
    t -= 1
