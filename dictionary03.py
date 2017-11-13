word = raw_input('Please enter a string: ')


word_dictionary = {}
for element in word:
    word_dictionary[element] = word.count(element)

print 'Count: '
for key in word_dictionary.iteritems():
    print key