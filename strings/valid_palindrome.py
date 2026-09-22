def is_palindrome(s):
    """
    Check whether a string is a palindrome.
    """

    cleaned = ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


# Example
text = "A man, a plan, a canal: Panama"

print(is_palindrome(text))
