da, db = map(int, input().split())
if da != 9 or db!=1:
    if db-da == 1:
        a = str(da)+'9'
        b = str(db)+'0'
        print(a,b,sep=' ')
    elif da-db == 0:
        a = str(da)+'1'
        b = str(db)+'2'
        print(a,b,sep=' ')
    else:
        print(-1)
else:
    print(9,10,sep=' ')

