import Queue

class TaskQueue:

    directionQueue = None
    floorQueue = None

    def __init__(self):
        self.directionQueue = Queue.Queue()
        self.floorQueue = Queue.Queue()

    def pushToDirectionQueue(self, directionType):
        self.directionQueue.put(directionType)

    def pushToFloorQueue(self, floorNumber):
        self.floorQueue.put(floorNumber)
