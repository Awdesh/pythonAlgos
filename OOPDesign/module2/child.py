from module1.Parent import Parent

class Child1(object):

    def __init__(self):
        print 'inside the child1 constructor.'

    def setUp(self):
        p = Parent()
        p.setUp()
        print 'inside Child1 set up'
        # super(Child1, self).setUp()
        # super(self).setUp()

    def tearDown(self):
        print 'inside Child1 tear down'        


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    c = Child1()
    c.setUp()
