# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def string_reverse(str1):

    rev_str1 = ''
    index = len(str1)
    while index > 0:
        rev_str1 += str1[ index - 1 ]
        index = index - 1
    return rev_str1
print(string_reverse('1234abcd'))