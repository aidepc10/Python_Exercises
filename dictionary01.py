my_zoo_animals = {'Unicorn': 'Cotton Candy House', 'Sloth': 'Rainforest Exhibit', 'Bengal Tiger': 'Jungle Box', 'Atlantic Puffin': 'Artic Exhibit', 'Rockhopper Penguin': 'Artic Exhibit'}
print 'Deleting sloth and bengal tiger from Dictionary: '

print my_zoo_animals

my_zoo_animals.pop('Sloth')
my_zoo_animals.pop('Bengal Tiger')
print 'Removing Sloth and Bengal Tiger from dictionary: ', my_zoo_animals
my_zoo_animals['Rockhopper Penguin'] = 'Any other'

print 'Changing Rockhopper Penguing value: ',my_zoo_animals