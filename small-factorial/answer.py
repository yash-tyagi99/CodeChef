try:
    t = int(input())
    for i in range(1,t+1):
        num = int(input())
        fact = 1
        for i in range(1,num+1):
            fact = fact*i
        print(fact)
except:  
    pass