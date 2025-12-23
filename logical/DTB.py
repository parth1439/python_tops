binary = int(input("Enter a binary number: "))

decimal = 0
base = 1   

while binary > 0:
    rem = binary % 10      
    decimal = decimal + rem * base
    binary = binary // 10    
    base = base * 2         

print("Decimal =", decimal)
