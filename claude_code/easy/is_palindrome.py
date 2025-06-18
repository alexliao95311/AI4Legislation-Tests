def is_palindrome(s):
    """
    Check if a string is a palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Step 1: Clean the string - keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]


# Test cases
def test_palindrome_function():
    """Test the palindrome function with various examples"""
    
    test_cases = [
        ("racecar", True),
        ("A man a plan a canal Panama", True),
        ("race a car", False),
        ("hello", False),
        ("Madam", True),
        ("No 'x' in Nixon", True),
        ("Mr. Owl ate my metal worm", True),
        ("", True),  # Empty string is considered a palindrome
        ("a", True),  # Single character is a palindrome
        ("Aa", True),
        ("12321", True),
        ("12345", False)
    ]
    
    print("Testing palindrome function:")
    print("-" * 40)
    
    for test_string, expected in test_cases:
        result = is_palindrome(test_string)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{test_string}' -> {result} (expected: {expected})")
    
    print("-" * 40)


# Run the tests
if __name__ == "__main__":
    test_palindrome_function()
    
    # Interactive examples
    print("\nTry some examples:")
    examples = ["racecar", "A man a plan a canal Panama", "hello world"]
    for example in examples:
        result = is_palindrome(example)
        print(f"is_palindrome('{example}') = {result}")