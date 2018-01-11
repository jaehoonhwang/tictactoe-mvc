class Player(object):

    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def set_name(self, name):
        self.name = name

    def set_marker(self, marker):
        self.marker = marker

    def return_name(self):
        return self.name

    def return_marker(self):
        return self.marker

    def __str__(self):
        return "Name: {0}, Marker: {1}".format(self.name, self.marker)

    def __eq__(self, other):
        return self.marker == other.marker
