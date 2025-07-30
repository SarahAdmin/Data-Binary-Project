def ConvertDectoOct(number): 
  oct_representation = oct(number) 
  return oct_representation 
  
if __name__ == "__main__": 
  user_one = intput('Enter a number: ') 
  oct_output = ConvertDectoOct(user_one) 
  print(f'In Octal: {oct_output}')
