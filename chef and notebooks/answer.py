tc=int(input())
for _ in range (tc):
    x,y,k,n=map(int,input().split())
    flag=0
    for i in range (n):
        p,c=map(int,input().split())
        if c<=k and p>=x-y:
            flag=1
    if flag==1:
        print("LuckyChef")
    else:
        print("UnluckyChef")