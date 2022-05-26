from excel_generator import BudgetExcelGenerator

class Flights(BudgetExcelGenerator):
    def __init__(self):
        super().__init__()
        self.flights = { }

    def add_flight(self, flight_Id, capacity):
        self.flights[flight_Id] = capacity

    def return_flight_value(self, key):
        try:
            return self.flights[key]
        except KeyError:
             print("The key was not found")
             raise

    def delete_flight(self,flight_Id):
        try:
            del self.flights[flight_Id]
        except KeyError:
            print("The key was not found")
            raise

    def print_flights(self):
        for my_val in self.flights:
            print("The fight ID is:",my_val ,"and the capacity is:",self.flights[my_val],".")


    def save_budget_items(self,file_name_and_path = 'default'):
        self.create_budget_list(self.flights)
        self.save_file_as(file_name_and_path)

flight_list = Flights()
flight_list.add_flight("FW234",50)
flight_list.return_flight_value("FW234")
flight_list.print_flights()
