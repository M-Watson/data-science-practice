'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''


input_n = input('What number do you want to choose? ')

n = int(input_n)


check_n = [i+1 for i in range(n)]

divisor = []
for number_to_check in check_n:

    mod = n % number_to_check

    if  mod == 0: divisor.append(number_to_check)


for checked_number in divisor:
    print(checked_number)
