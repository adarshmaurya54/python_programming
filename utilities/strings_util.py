def count_vowels(s, index=0): 
  vowels = 'aeiou' 
  if index == len(s): 
    return 0 
  return (1 if s[index].lower() in vowels else 0) + count_vowels(s, index + 1) 

def check_palindrome(str): 
  if len(str)<=1: 
    return True 
  if str[0].lower() != str[-1].lower(): 
    return False 
  return check_palindrome(str[1:-1]) 