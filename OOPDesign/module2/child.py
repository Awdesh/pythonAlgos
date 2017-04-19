from module1.parent import parent

class child1(parent):

    def __init__(self):
        print 'inside the child1 constructor.'

    def setUp(self):
        p = parent('A', 120000)
        print 'Name is: %s' % p.name
        print 'Salary is: %s' % p.salary
        print 'Class member: %s ' % p.parentAttr
        print p.classAttr
        p.setUp()
        print 'inside Child1 set up'
        c1 = child1()
        c1.tearDown()

        # super(Child1, self).setUp()
        # super(self).setUp()

    def tearDown(self):
        print 'inside Child1 tear down'


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    c = child1()
    c.setUp()
