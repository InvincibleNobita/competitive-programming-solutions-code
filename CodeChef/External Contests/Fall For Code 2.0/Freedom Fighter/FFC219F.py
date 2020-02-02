def sorting(l):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j], l[i]
    return l

t = int(input())
k = 0
while k < t:
    n, p = map(int, input().split())
    s = list(map(int, input().split()))
    l = sorting(s)
    count = 0
    for item in l:
        if item <= p:
            p -= item
            count += 1
            if p == 0:
                break
        else:
            break
    print(count)
    k += 1


"""
Test Cases:

1
3 1000000000
1000000 1000000 1000000
"""
