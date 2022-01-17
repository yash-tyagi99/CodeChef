try:
    withdraw,total=map(str,input().split())
    withdraw=int(withdraw)
    total=float(total)
    if withdraw%5==0 and withdraw + 0.50<=total:
        print(total-withdraw-0.50)
    else:
        print(total)
except:
    print("Data not verified")