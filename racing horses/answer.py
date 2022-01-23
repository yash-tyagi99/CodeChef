t=int(input())
for k in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a=l[1]-l[0]
    for j in range(1,n):
        if((l[j]-l[j-1])<a):
            a=l[j]-l[j-1]
    print(a)