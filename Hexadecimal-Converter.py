def ConvertDectoHex(number): 
  return hex(number)[2:].upper()
  
ConvertDectoHex(int(input('Enter your number: ')))
