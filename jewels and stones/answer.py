t=int(input())
for i in range (t):
    s=input()
    j=input()
    l=[i for i in j if i in s]
    print(len(l))