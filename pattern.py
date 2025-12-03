# """ for i in range (1,6):
#     for j in range (1,6):
#         print("*",end=" ")
#     print() """



#*
#**
#***
#****
#*****
# """ r=5
# for i in range (1,6):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print() """
    
#*****
#****
#***
#**
#*
# """ n=5
# for i in range (n,0,-1):
#     for j in range (i):
#         print("*",end=" ")
#     print() """


#54321
#4321
#321
#21
#1
# n=5
# for i in range (n,0,-1):
#     for j in range (i,0,-1):
#         print(j,end=" ")
#     print()

#    *
#   **
#  ***
# ****
#*****
# """ n =6
# for i in range (1,6):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range (1,i+1):
#         print("*",end="")
#     print() """

#*****    
#****   
#***
#**
#*

# """ for i in range (5,0,-1):
#     for j in range(6,i-1):
#         print("",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print() """


# """ for i in range (5,0,-1):
#     for j in range (1,i+1):
#         print("*",end="")
#     print() """

#    *
#   ***
#  *****
# *******
#*********
# """ for i in range (1,6):
#     for j in range (1,6-i):
#         print(" ",end="")
#     for k in range(1,(2*i-1)+1):
#         print("*",end="")
#     print()"""


#*********
# *******
#  *****
#   ***
#    *
# """ for i in range (5,0,-1):
#     for j in range (1,6-i):
#         print(" ",end="")
#     for k in range(1,(2*i-1)+1):
#         print("*",end="")
#     print()  
#  """

#12345
#1234
#123
#12
#1
# """ for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()  """ 
# """ n = 5
# mid = n//2+1

# for i in range (n):
#     for j in range (n-i):
#         print(" ",end="")
#     for k in range (1,(2*i-1)+1):
#         print("*",end="")
#     print()
#  """




#1
#23
#456
#78910
# """ rows=1
# for i in range (1,5):
#     for j in range (i):
#         print(rows,end="")
#         rows+=1
#     print() """


for i in range (5,0,-1):
    for j in range(1,1+i):
        print(j,end="")
    print()

# a=50
# b=3

# print("the value of:",a,"+",3,"is:",a+b)
# print("the value of:",a,"-",3,"is:",a-b)
# print("the value of:",a,"*",3,"is:",a*b)
# print("the value of:",a,"/",3,"is:",a/b)
# print("the value of:",a,"//",3,"is:",a//b)
# print("the value of:",a,"**",3,"is:",a**b)


num=int(input("enter a number"))

if(num < 0):
    print("number is negative")
elif(num==0):
    print("number is zero")
else:
    print("number is positive")