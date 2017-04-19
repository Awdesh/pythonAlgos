class Maps:
    # class member
    list = []

    def __init__(self):
        pass

    def put(self, item):
        hc = self._get_hash_code(item)
        Maps.list.append(hc)

    def get(self, item):
        hc = self._get_hash_code(item)
        return hc

    def get_length(self):
        return len(Maps.list)

    @staticmethod
    def _get_hash_code(item):
        print ord(item)
        return ord(item) * 3.14

if __name__ == '__main__':
    m = Maps()
    m.put('a')
    i = m.get('a')
    print i
    print m.list # This will call list from instance dict.
    print Maps.list
    print m.get_length()
