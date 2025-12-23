# # def message():
# #     print("hello,good morning")
# # message()
# # message()

# # def square(a):
# #     print(f"square of {a} is {a*a}")
# # square(5)

# # def sum(a,b):
# #     print(f"sum is {a} and {b} is {a+b}")
# # sum(15,15)

# # def mod(a,b):
# #     c=a%b
# #     return c
# # mod(10,2)
# # a=10
# # def test():
# #     global a
# #     a = 20
# #     print(a)
# # print(a)
# # test()

# # def square(a):
# #     print(a*a)
# #     a+=1
# #     if a<20:
# #         square(a)
# # square(10)


# # a=10
# # def test():
# #     global a
# #     a=20
# #     print(a)
# # print(a)
# # test()

# # def avg():
# #     a=int(input("enter a number"))
# #     b=int(input("enter a number"))
# #     c=int(input("enter a number"))

# #     average=(a+b+c)/3
# #     print(average)
# # avg()

# # def goodday():
# #     print("good day")
# # goodday()

# def factorial(n):
   
#     if n==1:
#         return 1
#     else:
#        return n*factorial(n-1) 
# num=int(input("enter a number"))
# print("factoral number is",factorial(num))

# subjects =["python","android","php","java","sql"]

# k=filter(lambda x:x.count('a'),subjects)
# print(list(k))



from functools import reduce

l = [1,2,30,40,51,6,7] 
k = reduce(lambda x,y:x+y,l)
k = reduce(lambda x,y : x if x<y else y,l)
print(k)












