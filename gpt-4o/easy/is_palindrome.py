import string

def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is the same forwards and backwards
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))                         # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("No lemon, no melon"))              # True
print(is_palindrome("Hello"))                           # False
print(is_palindrome("12321"))                           # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True