from .button import Button

class Car:

    button = None

    def __init__(self):
        self.button = Button()

    def call(self):
        # query queue and submit a task
        # queries directionqueue to find next available
        # add an item in the directionqueue
        self.button.pressDirectionButton(1)
        pass

    def moveUp(self):
        # queries floorQueue to determine direction
        pass

    def moveDown(self):
        pass

    def openDoor(self):
        pass

    def classDoor(self):
        pass
