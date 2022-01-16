n = int(input())
sum1 = 0
sum2 = 0
lead = 0
diff = 0
for i in range(n):
    (a,b)=map(int,input().split( ))
    sum1 += a
    sum2 += b
    if sum1 > sum2:
        diff = sum1 - sum2
        if diff > lead:
            lead = diff
            winner = 1
    else:
        diff = sum2 - sum1
        if diff > lead:
            lead = diff
            winner = 2
print(winner,lead)
    

