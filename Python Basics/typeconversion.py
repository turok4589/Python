name = 'Andrei Neagoie'
age = 50
relationship_status = 'single'

relationship_status = 'it\'s complicated';

print(relationship_status)

#let's create a program that guesses your age
currentyear = 2022
birthyear = input("What year were u born: ")

#input is usually a string

print("You are " + str((currentyear - int(birthyear))) + " years old")

#also could have done

age = currentyear - int(birthyear)

print(f'Your age is: {age}, damn you old')

#Formatted string