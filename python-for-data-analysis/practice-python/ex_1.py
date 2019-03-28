# URL: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''


import datetime
now = datetime.datetime.now()
year = now.year


name = input('Hello, what is your name?  ')
age = input('....and your age?  ')

age = int(age)
years_to_100 = 100 - age

year_of_100 = years_to_100 + year

#line = 'Hello {} you will be 100 in {}'.format(name,str(year_of_100))
line = 'Hello {} you will be 100 in {}\n'.format(name,str(year_of_100))
print(line)


repeat_times = input('How many times would you like to repeat that message?')

i_end = int(repeat_times)

i = 0
while i  < i_end:
    print(line)
    i+=1
