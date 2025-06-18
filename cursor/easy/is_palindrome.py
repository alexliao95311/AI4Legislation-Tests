def is_palindrome(s):
    # Step 1: Clean the string
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome("Was it a car or a cat I saw?"))    # True
print(is_palindrome("hello"))                           # False
print(is_palindrome("Madam, I'm Adam"))                 # True
