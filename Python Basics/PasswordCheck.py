username = input('Enter Username: ')
password = input('Enter Password: ')

if (len(username) > 0 and len(password) > 0):
    length = len(password)
    print(f'{username}, your password ' + '*' * length + f' is {length} letters long')
    print('{0}, your password '.format(username) 
    + '*' * length + ' is {0} letters long'.format(length))

  #in his example he called the len function inside the {}. That's something you can do
