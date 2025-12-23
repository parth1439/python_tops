num=int(input("enter a binary"))
decimal=0
base=1

while(num>0):
    rem=num%10
    num=num//10
    decimal=decimal+str(rem)*base
    print("binary",decimal)
    basse=base*2


