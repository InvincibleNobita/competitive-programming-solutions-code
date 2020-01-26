from collections import deque

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    count = 1
    q = deque(l[:5])
    if l[1] < l[0]:
        count += 1
    if l[2] < l[0] and l[2] < l[1]:
        count += 1
    if l[3] < l[0] and l[3] < l[1] and l[3] < l[2]:
        count += 1
    if l[4] < l[0] and l[4] < l[1] and l[4] < l[2] and l[4] < l[3]:
        count += 1
    for i in range(5,n):
        if l[i] < q[0] and l[i] < q[1] and l[i] < q[2] and l[i] < q[3] and l[i] < q[4]:
            count += 1
        q.append(l[i])
        q.popleft()
    print(count)
    t -= 1
