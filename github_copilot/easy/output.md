Palindrome Checker Function
A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward, ignoring spaces, punctuation, and case sensitivity.

Here's a Python function that checks if a given string is a palindrome:

Explanation for beginners:
We convert the input string to lowercase using .lower() to make our comparison case-insensitive.
We create a new string clean_s that contains only letters and numbers (no spaces or punctuation) by:
Looping through each character in the string
Using isalnum() to check if it's a letter or number
Adding it to our clean string if it is
We compare the clean string with its reverse:
clean_s[::-1] creates a reversed version of the string using Python's slice notation
If they're equal, it's a palindrome!
Example test cases:
This approach ensures we properly handle spaces, punctuation, and case differences while checking if the text is a palindrome.