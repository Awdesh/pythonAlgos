class Anagram:

    dict = {}

    def __init__(self):
        Anagram.dict = {}

    def is_anagram(self,s1, s2):
        print '***** starting *****'

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
                key = Anagram.dict.get(i)
                key -= 1
                # import pdb; pdb.set_trace()
                Anagram.dict[i] = key

        print Anagram.dict

        for i in Anagram.dict.keys():
            if Anagram.dict.get(i) == 0:
                del Anagram.dict[i]

        if len(Anagram.dict) == 0:
            print Anagram.dict
            return True
        else:
            return False

if __name__ == '__main__':
    a = Anagram()
    b = a.is_anagram('aba', 'bab')
    print b
    o = Anagram()
    c = o.is_anagram('aba', 'baa')
    print c
