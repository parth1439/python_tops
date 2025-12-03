num = int(input("Enter a number: "))
digits = len(str(num))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum+= digit ** digits
    temp = temp // 10

if sum == num:
    print(num, "is an aramstrong number")
else:
    print(num,"is not an aramstorng number")
