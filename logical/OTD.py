octal = int(input("Enter an octal number: "))

decimal = 0
base = 1   

while octal > 0:
    rem = octal % 10        
    decimal = decimal + rem * base
    octal = octal // 10    
    base = base * 8         

print("Decimal =", decimal)
