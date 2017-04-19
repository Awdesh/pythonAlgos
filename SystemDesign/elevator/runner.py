import Queue
from .button import Button
from .car import Car

class ElevatorController:

    car = None

    def __init__(self):
        self.car = Car()
        self.reset()

    def reset(self):
        self.round = 1

    # @classmethod
    def run(self):
        # fq = Button.floorQueue
        self.car.call()
