# Write a Python function that accepts a string and
# calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def string_test(str1):
    letters={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in str1:
        if i.isupper():
           letters["UPPER_CASE"]+=1
        elif i.islower():
           letters["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str1)
    print ("No. of Upper case characters : ", letters["UPPER_CASE"])
    print ("No. of Lower case Characters : ", letters["LOWER_CASE"])

string_test('The quick Brow Fox')