n = int(input("Enter a number: "))
digits = len(str(n))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum+= digit ** digits
    temp = temp // 10

if sum == n:
    print(n, "is an aramstrong number")
else:
    print(n,"is not an aramstorng number")
