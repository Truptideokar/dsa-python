def reverse_string(s):
    """
    Reverse a string using two pointers.
    """

    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)


# Example
text = "hello"

print(reverse_string(text))
