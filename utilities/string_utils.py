def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1] 