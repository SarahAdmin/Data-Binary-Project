myNum = int(input('Enter a decimal number: '))
x = bin(myNum)[2:]
y = oct(myNum)[2:]
z = hex(myNum)[2:].upper()
dec = int(myNum)
print(f'In Binary {x}')
print(f'In Octal {y}')
print(f'In Hexadecimal {z}')
print(f'In Decimal {dec}')
