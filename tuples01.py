print 'Printing a tuple whose values are even numbers i the given tuple: '

my_tuple = (1,2,3,4,5,6,7,8,9,10)
print my_tuple

new_tuple = ()

temp_list = []

for element in my_tuple:
    if element%2 ==0:
        temp_list.append(element)

new_tuple = (temp_list)

print 'My new tuple: ', new_tuple

