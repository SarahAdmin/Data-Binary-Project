def ConvertDectoBinary(number): 
    binary_representation = bin(number)[2:]
    return binary_representation 

if __name__ == "__main__": 
    user_input = int(input('Enter a number: '))
    bin_output = ConvertDectoBinary(user_input)
    print(f'In Decimal: {user_input}')
    print(f'In Binary: {bin_output}')
