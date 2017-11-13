from math import tan
from math import radians

print "Welcome, let's calculate perimeter and area of a regular polygon\n"
side_num = input ('Please introduce the number of sides: ')
large = input('Please introduce the large (in cm) of each side: ')

perimeter = side_num * large

angle = (360/side_num)
rad = radians(angle)
tang = tan(rad/2)
ap = large/(2*tang)

area = (perimeter * ap)/2

print 'The perimeter of this ploygon is: ', perimeter, ' cm'
print 'The area of this polygon is: ', area, ' cm2'

