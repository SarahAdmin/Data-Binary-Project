def DectoBin(num): 
    bin_representation = bin(num)[2:]
    return bin_representation 
def DectoHex(num): 
    hex_representation = hex(num)[2:].upper()
    return hex_representation 
def DectoOct(num): 
    oct_representation = oct(num)[2:] 
    return oct_representation 

if __name__ == "__main__": 
    user_input = int(input('Enter a decimal number: '))
    output_1 = DectoBin(user_input)
    output_2 = DectoHex(user_input)
    output_3 = DectoOct(user_input)
    print(f'In Decimal: {user_input}')
    print(f'In Binary: {output_1}')
    print(f'In Hexadecimal: {output_2}')
    print(f'In Octal: {output_3}')