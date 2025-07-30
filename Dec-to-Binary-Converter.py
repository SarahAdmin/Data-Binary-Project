def ConvertToBin(number): 
  if (number < 64): 
      print(bin(number)[2:])
      print('Lower Than Eight Digits')
  else: 
    print(bin(number)[2:]) 
    print('Greater than Eight')
    
ConvertToBin(int(input('Enter your Number: ')))
 
