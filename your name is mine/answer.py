def isSub(s1,s2):
    i = 0
    for c in s2:
        if c == s1[i] : i+=1
        if i==len(s1) : return True
    return False
for _ in range(int(input())):
    m,w = map(str,input().split())
    if(isSub(m,w) or isSub(w,m)) : print("YES")
    else : print("NO")