#!/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

print('Hello, world')
# prints hello world in the interpreter
user_name = input('Enter your name ')
# variable user_name holds in memory the name entered here
location = input('Where are you from? ')
# variable holding the location of the user
number1 = input('Please enter your first number: ')
number2 = input('Please enter your second number: ')
final = int(number1) + int(number2)
print('Hello', user_name, 'from', location)
print('The sum of {0} and {1} numbers equals {2}'.format(number1,number2,final))
# prints hello + name of user + location of user
