
def IsPalindrome (text, left = 0, right = 0):

    # Default value of right
    if right == 0:
        right = len(text) - 1

    # Number of characters in substring
    n = right - left + 1

    # Base case
    if n <= 1:
        return True

# Check if first and last characters are equal
    if text[left] != text[right]:
        return False

# Recursive call
    return IsPalindrome(text, left + 1, right - 1)

# MAIN PROGRAM
text = input("Enter String: ")
if IsPalindrome(text):
    print("The string is a palindrome")
else:
    print("The string is is not a palindrome")

