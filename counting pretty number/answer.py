t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    c = 0
    for j in range(a,b+1):
        s = j % 10
        if s==2 or s==3 or s==9 :
            c = c+1
    print(c)