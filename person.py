class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f'Hello {self._first_name} {self._last_name}')

    @property
    def first_name(self):
        print("this is the getter method")
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print("we are in the setter now")
        self._first_name = new_first_name
