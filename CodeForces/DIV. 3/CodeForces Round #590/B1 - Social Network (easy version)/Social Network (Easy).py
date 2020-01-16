from array import array

n, k = map(int, input().split())
ids = array('i', map(int, input().split()))
l = array('i')
for var in ids:
    if var in l:
        pass
    else:
        l.insert(0,var)
        if len(l) > k:
            l.pop()
print(len(l))
print(*l,sep=" ")
