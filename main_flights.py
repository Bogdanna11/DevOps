from passenger import Passenger
from flight import Flight
from flights import Flights

person1 = Passenger("bogdana","rus",32312132)
person2 = Passenger("Sonia","rus",32323123123213)
flight1 = Flight("FW232",300)
flight1.add_passengers(person1)
flight1.add_passengers(person2)
flight_list = Flights()
flight_list.add_flight("FW234",50)
flight_list.add_flight("FW134",50)
flight_list.print_flights()
flight_list.save_budget_items()

print(flight1)
