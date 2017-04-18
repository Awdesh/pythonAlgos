#!/usr/bin/python
class DataStructure:

    def __init__(self):
        print 'inside constructor'

    def print_list(self):
        print '***** LIST ******'

        list = ['aa', 1, 1.0, 131212343241, ]

        print list[0]
        print list[1]
        print list[2]
        print list[3]

        #  left to the colon is index (inclusive), right to it is element (exclusive).
        print list[1:3]
        print list[1:]
        print list[:1]
        print list[:3]

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
