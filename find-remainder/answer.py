try:
    t = int(input())
    for i in range(t):
        (a, b) = map(int, input().split(' '))
        temp = a%b
        print(temp)
except:
    pass