zoo_animals = ['elephant', 'zebra', 'tiger', 'lion']

print 'Adding cheetah to the list:'
zoo_animals.append('cheetah')
print 'Number of Items on zoo_animals: ', zoo_animals.__len__()
print 'New list: ', zoo_animals

print 'Replacing lion:'
lion_index = zoo_animals.index('lion')
print 'lion index: ',lion_index
zoo_animals.remove('lion')
print 'Inserting penguin in lion index value'
zoo_animals.insert(lion_index,'penguin')
print 'New list: ', zoo_animals
zoo_animals

print 'Removing zebra from list:'
zoo_animals.remove('zebra')
print 'New list: ', zoo_animals