import person
class Employee(person.Person):
    def __init__(self,fname,lname,department):
        super().__init__(fname,lname)
        self._department = department
    def print(self):
        super().print()
        print(f"You are from the {self._department} department.\n ")

