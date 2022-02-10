t = int(input())
for i in range(t):
    n = int(input())
    if (360%n == 0):
        print('y')
    else:
        print('n')
    if(n<=360):
        print('y')
    else:
        print('n')
    if((n*(n+1)//2) <= 360):
        print('y')
    else:
        print('n')