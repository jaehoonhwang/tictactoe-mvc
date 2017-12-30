
class Space(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = -1

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return "Space @({0}, {1}) with value: {2}".format(self.x, self.y, self.value)
