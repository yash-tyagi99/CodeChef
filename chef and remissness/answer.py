t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    print(max(a),a[0]+a[1])