#!/usr/bin/python

str = 'Hello World!'

print str          # Prints complete string
print str * 5
list = ['aa', 1, 1.0, 131212343241, ]

print list[0]
print list[1]
print list[2]


print list[3]

#  left to the colon is index , right to it is element.
print list[1:3]
print list[1:]
print list[:1]
print list[:3]

dict = {}
dict['key1'] = 'value1'
dict[1] = 10
dict[2.0] = 13123123

print dict

var = 500

if var == 100:
    print 'inside if'
elif var == 50:
    print 'inside elif'
else:
    print 'else'