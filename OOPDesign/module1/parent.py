class parent:
    parentAttr = 0

    def __init__(self, name, salary):
        print 'inside the parent constructor.'
        self.name = name
        self.salary = salary
        parent.parentAttr += 1

    def print_name_salary(self):
        print 'Instance member is %d' % self.name

    def setUp(self):
        print 'inside parent set up'

    def tearDown(self):
        print 'inside parent tear down'
