num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i    # multiply fact with i
    i = 1         # increase i in every step

print("Factorial =", fact)
