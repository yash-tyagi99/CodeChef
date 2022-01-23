t = int(input())
for i in range(t):
    l = int(input())
    s = list(map(int,input().split()))
    k = int(input())
    d = s[k-1]
    s.sort()
    print(s.index(d)+1)