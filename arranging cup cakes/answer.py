import math
t = int(input())

for i in range(t):
    n = int(input())
    mini = n
    for j in range(1,int(math.sqrt(n)+1)):
        if(n%j==0):
            rem = n/j
            diff = abs(rem-j) 
            if(diff <mini):
                mini = diff
    print(int(mini))