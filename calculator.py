num1=float(input("enter a number:"))
num2=float(input("enter a number:"))

print("select opertor: + - * /")
op=input("enter opertor:")

if op =='+':
    print("result:",num1+num2)
elif op =='-':
    print("result:",num1-num2)
elif op =='*':
    print("result:",num1*num2)
elif op =='/':
    if num2 !=0:
        print("result:",num1/num2)
    else:
        print("error! devision by zero.")
else:
    print("invalid opertor")