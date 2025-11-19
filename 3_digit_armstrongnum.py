for num in range(100, 1000):   # 3-digit numbers start from 100 to 999
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10        # last digit
        sum += digit ** 3        # cube of digit
        temp //= 10              # remove last digit
    
    if sum == num:
        print(num)
