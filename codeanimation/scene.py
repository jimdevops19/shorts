# Python cool magic methods:


class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f'Person({self.name})'

    def __len__(self):
         return len(str(self.name))

