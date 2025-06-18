def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    A palindrome is a string that reads the same forward and backward,
    ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Convert to lowercase
    s = s.lower()
    
    # Create a clean version with only alphanumeric characters
    clean_s = ""
    for char in s:
        if char.isalnum():  # Keep only letters and numbers
            clean_s += char
    
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Test cases
print(is_palindrome("racecar"))                      # True
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("Was it a car or a cat I saw?")) # True
print(is_palindrome("hello"))                       # False
print(is_palindrome("Madam, I'm Adam"))             # True
print(is_palindrome("12321"))                       # True

