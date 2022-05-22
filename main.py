import customer
import employee
import person
import random
if random.randint(0,1) == 0:
    chosen_person = customer.Customer('Bogdana','Rus','Cluj')
else:
    chosen_person = employee.Employee('Diana','Smith','sales')
chosen_person.print()
