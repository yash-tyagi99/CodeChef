t = int(input())
for i in range(t):
    (a,b,c)=map(int,input().split( ))
    # sum = a+b+c
    if a+b+c == 180:
        print('YES')
    else:
        print('NO')