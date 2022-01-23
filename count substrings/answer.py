t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = s.count("1")
    print((c*(c+1))//2)