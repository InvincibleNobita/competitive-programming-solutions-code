t = int(input())
while t:
    n = int(input())
    s = []
    count = [0]*10
    while n:
        s.append(input())
        n-=1
    for item in s:
        for i in range(0,10):
            if item[i] == '1':
                count[i] += 1
    j = [x for x in count if x%2!=0]
    print(len(j))
    t -= 1
