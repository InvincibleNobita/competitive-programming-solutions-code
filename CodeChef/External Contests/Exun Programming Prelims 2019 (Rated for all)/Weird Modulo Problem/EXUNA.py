t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    cost = min(arr)
    print(cost)
    t -= 1
