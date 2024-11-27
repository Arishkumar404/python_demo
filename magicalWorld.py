n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    if l[0]*l[2]+l[1]<=l[3]:
        print("YES")
        print("no")
    else:
        print('yes')
