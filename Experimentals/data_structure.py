#!/usr/bin/python
class DataStructure:

    def __init__(self):
        print 'inside constructor'

    # In python list is been used widely instead of an array.
    def print_list(self):
        print '***** LIST ******'

        # There's no native array in python.
        list = ['aa', 1, 1.0, 131212343241, ]

        print list[0]
         #  left to the colon is index (inclusive), right to it is element (exclusive).
        print list[1:3]
        print list[1:]
        print list[:1]
        print list[:3]

        print list.count('aa')
        print len(list)

        list.append(3)
        list.append('4')
        print list
        print list[-4]

    def print_dictionary(self):
        print '****** Dictionary *****'

        dict = {}
        dict['key1'] = 'value1'
        dict[1] = 10
        dict[2.0] = 13123123

        print dict

    def print_string(self):
        print '***** String ******'

        str = 'Hello World!'
        print str          # Prints complete string
        print str * 5

if __name__ == "__main__":
    ds = DataStructure()
    ds.print_string()
    ds.print_list()
    ds.print_dictionary()
