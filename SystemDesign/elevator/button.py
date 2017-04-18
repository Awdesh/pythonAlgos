from .taskqueue import TaskQueue

class Button:

    tq = None

    def __init__(self):
        self.tq = TaskQueue()
        # self.floorQueue = Queue.Queue()

    def pressDirectionButton(self, directionType):
        self.tq.pushToDirectionQueue(directionType);

    def pressFloorButton(self, floorNumber):
        button = cls()
        self.tq.pushToFloorQueue(floorNumber)
