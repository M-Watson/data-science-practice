'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''


input_string = input('Please input a string: ')
check_string = ''
i = len(input_string)
while i > 0:

    check_string = check_string + input_string[i-1]
    i -= 1




if input_string == check_string:
    print('{} is a palindrome!'.format(input_string))
else:
    print('{} is not a palindrome :/'.format(input_string))
