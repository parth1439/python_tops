# n=int(input("enter a number"))
# fact=0
# i=1

# while(i<=n):
#     if(n%i==0):
#         fact=fact+1
#     i=i+1
# if(fact==2):
#     print("prime number")
# else:
#     print("not a prime number") 



# 1 to 100 prime number
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)




