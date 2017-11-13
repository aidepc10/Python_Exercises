my_list = [1,4,9,16,25,36,49,64,81,100]

print my_list

new_list = []

for element in my_list:
    if (element%2) != 0 and my_list.index(element) != 0 and my_list.index(element) != my_list.__len__() - 1:
        new_list.append(element)

print new_list

