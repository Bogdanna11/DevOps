class Passenger:
    def __init__(self,first_name,last_name,passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
    def __repr__(self):
        return f"\n First name:{self.first_name}\n Last name:{self.last_name} \n Passport number:{self.passport_number}\n"
