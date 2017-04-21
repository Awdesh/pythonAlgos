class Anagram:

    dict = {}

    def __init__(self):
        Anagram.dict = {}

    def is_anagram(self,s1, s2):
        print '***** starting *****'

        print '***** convert input strings to lowercase'
        s1 = s1.lower()
        s2 = s2.lower()

        for i in s1:
            if i not in Anagram.dict:
                Anagram.dict[i] = 1
            else:
                Anagram.dict[i] += 1

        print Anagram.dict

        for i in s2:
            if i not in Anagram.dict:
                return false
            else:
                Anagram.dict[i] -= 1

        print Anagram.dict

        for i in Anagram.dict.keys():
            if Anagram.dict.get(i) == 0:
                del Anagram.dict[i]

        if len(Anagram.dict) == 0:
            print Anagram.dict
            return True
        else:
            return False

    def is_anagram_1(self, str1, str2):
        str1_list = list(str1)
        str1_list.sort()

        str2_list = list(str2)
        str2_list.sort()

        return (str1_list == str2_list)

if __name__ == '__main__':
    a = Anagram()
    # Test Case-: 1
    b = a.is_anagram('aba', 'bab')
    print b
    val = a.is_anagram_1('aba', 'bab')
    print val

    o = Anagram()
    # Test Case-: 2
    c = o.is_anagram('car', 'arc')
    print c
    # Test Case-: 3
    d = o.is_anagram('Aba', 'baa')
    print d
