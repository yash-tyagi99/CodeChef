try:
    t = int(input())
    for i in range(t):
        a,b,c=map(int,input().split( ))
        if(a>b and a>c):
            if(b>c):
                print(b)
            else:
                print(c)
        elif(b>a and b>c):
            if(a>c):
                print(a)
            else:
                print(c)
        else:
            if(a>b):
                print(a)
            else:
                print(b)
        # if(a>b and b>c):
        #     print(b)
        # elif(b>c and c>a):
        #     print(c)
        # else:
        #     print(a)
        
            
except:
    pass
        