def decimalToBinary(num):
    '''This function converts decimal number
    to binary and prints it'''
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

# decimal number
number = float(input("Enter any decimal number: "))
decimalToBinary(number)