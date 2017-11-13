birthday = {}

birthday['Diana'] = 'February 24'
birthday['Clari'] = 'April 03'
birthday['Brenda'] = 'April 10'
birthday['Rafa'] = 'April 28'
birthday['Beli'] = 'May 05'
birthday['Ray'] = 'June 10'
birthday['Carlos'] = 'November 12'
birthday['Ernesto'] = 'November 16'

print birthday

print 'Welcome'

while True:
    name = raw_input('Please enter a name: ')
    show_birthday = birthday.get(name)

    if name in birthday:
        print 'The Birthday of ', name, ' is: ', show_birthday
        break
    else:
        print 'name not found'

