#Integers are whole numbers
print(type(2+4)) #prints the type of this value
print(bin(5))
print(int('0b101', 2)) #This number is base 2 convert it to integer. Returns 5
#'0b' is used to tell the computer that the number you typed is a base-2 number not a base-10 number. 
long_string = '''
WOW
0 0
---'''
print(long_string)

name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old')
print('hi {}. You are {} years old'.format(name, age))

greet = 'hellloooo'
print(greet[0:8])

print('Your age is ' + str(age))