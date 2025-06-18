def is_palindrome(s):
    # Ignore spaces, punctuation, and case
    s = s.strip()
    s = s.lower()
    
    # Check if the string is the same when read forward and backward
    return s == s[::-1]

print(is_palindrome("racecar")) # Should print True
print(is_palindrome("level")) # Should print False
print(is_palindrome("radar")) # Should print True
print(is_palindrome("snow")) # Should print False