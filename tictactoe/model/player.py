class Player(object):

    def __init__(self, name, marker):
        self.Name = name
        self.Marker = marker

    def set_name(self, name):
        self.Name = name

    def set_marker(self, marker):
        self.Marker = marker

    def return_name(self):
        return self.Name

    def return_marker(self):
        return self.Marker
