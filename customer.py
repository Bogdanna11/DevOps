import person
class Customer(person.Person ):
     def __init__(self,fname,lname,address):
          super().__init__(fname,lname)
          self._address = address
     def print(self):
         super().print()
         print(f'Address: {self._address}.\n')
