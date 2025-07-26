def ConvertToBin(number): 
  if (number < 64): 
      print(bin(number))
      print('Lower Than Eight Digits')
  else: 
    print(bin(number)) 
    print('Greater than Eight')
    
ConvertToBin(int(input('Enter your Number: ')))
 
