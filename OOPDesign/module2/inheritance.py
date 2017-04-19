class Parent:

    def __init__(self):
        print 'inside the parent constructor.'

    def setUp(self):
        print 'inside parent set up'

    def tearDown(self):
        print 'inside parent tear down'


class Child1(Parent, object):

    def __init__(self):
        print 'inside the child1 constructor.'

    def setUp(self):
        print 'inside Child1 set up'
        super(Child1, self).setUp()
        # super(self).setUp()

    def tearDown(self):
        print 'inside Child1 tear down'


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    c = Child1()
    c.setUp()
