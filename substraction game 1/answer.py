import math
t = int(input())
for i in range(t):
    n = int(input())
    l=list(map(int,input().split()))
    a=l[0]
    for i in range(1,n):
        a=math.gcd(a,l[i])
    print(a)