class Passenger:
    def __init__(self,first_name,last_name,passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
    def __repr__(self):
        return f"\n First name:{self.first_name}\n Last name:{self.last_name} \n Passport number:{self.passport_number}\n"
class Flight():
    def __init__(self,flight_number,capacity):     
        self.flight_number = flight_number
        self.capacity = capacity     
        self.passengers = []      
    def add_passengers(self,passenger):
        if self.open_seats()==0:
            return False
        else: 
            self.passengers.append(passenger)
            return True
    def open_seats(self):
        return  self.capacity - len(self.passengers)
    def __repr__(self):
        print(f" The flight number: {self.flight_number} with a capacity {self.capacity} has the following passengers:")
        for i in range(len(self.passengers)):
            print(self.passengers[i])
 
person1 = Passenger("bogdana","rus",32312132)
person2 = Passenger("Sonia","rus",32323123123213)
flight1 = Flight("FW232",300)
flight1.add_passengers(person1)
flight1.add_passengers(person2)

print(flight1)
