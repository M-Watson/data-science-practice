'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''


input_number = input('What number do you want to choose? ')
input_n = input('What number would you like to check if {} is divisible by? '.format(input_number))

n = int(input_n)
number_int = int(input_number)

mod = number_int % 2
mod_4 = number_int % 4
mod_n = number_int % n


if  mod == 0:
    is_even = True
    if mod_4 == 0:
        print('{} is even and divisible by 4'.format(number_int))
    else:
        print('{} is even'.format(number_int))
else:
    is_even = False
    print('{} is odd'.format(number_int))


if mod_n == 0:
    print('{} is divisble by {}'.format(number_int,n))
else:
    print('{} is not divisble by {}'.format(number_int,n))    
