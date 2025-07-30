def ConvertDectoOct(number): 
  oct_representation = oct(number)[2:] 
  return oct_representation 
  
if __name__ == "__main__": 
  user_one = input('Enter a number: ') 
  oct_output = ConvertDectoOct(user_one) 
  print(f'In Octal: {oct_output}')
