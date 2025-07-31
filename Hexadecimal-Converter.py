def ConvertDectoHex(number): 
  hex_representation = hex(number)[2:].upper()
  return hex_representation
  
if __name__ = "__main__": 
   user_input = int(input('Enter a number: ')) 
   hex_output = ConvertDectoHex(user_input) 
   print(f'In Decimal: {user_input}') 
   print(f'In Hexadecimal: {hex_output}')
