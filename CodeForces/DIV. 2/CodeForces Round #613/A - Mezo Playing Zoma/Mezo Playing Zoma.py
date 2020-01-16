n = int(input())
s = input()
nega,posi = 0,0
for item in s:
    if item=="L":
        nega-=1
    else:
        posi+=1
print(posi-nega+1)
