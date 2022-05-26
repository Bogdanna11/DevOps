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
        print("We have the passengers :")
        for i in range(len(self.passengers)):
            print(self.passengers[i])

