Loops : 

list_data = [1,2,3,4,5]
embedded_list = [[1,2,3],[4,5,6]]

dict_data = {
1: {“name”:”Bronson”,”money: “$0.05”},
2: {“name”: “Natasha”,money:  “$1.45”},
3: {“name”: “Sonia”,money: “$2.55”}}

DISPLAY DATA IN A LIST: 
for num in list_data: 
    print(num*2) 
    
CHECKING FOR VALUES IN A LIST : 
for num in list_data:
     if num ==3:
        print(“I found 3”)
     elif num > 3: 
        print(“I have gone too far”)
     else:
        print(“Its too soon”)
    
IMPORTANT : use the breakpoints to check at each point what is happening !!!
DISPLAY DATA IN  NESTED LIST: 
for data in embedded_list:
    print(data) 
    for num in data: 
         print(num)
         
DISPLAY DATA IN THE DICTIONARY :
dict_data = {
1: {“name”:”Bronson”,”money: “$0.05”},
2: {“name”: “Natasha”,money:  “$1.45”},
3: {“name”: “Sonia”,money: “$2.55”}}

for item in dict_data.values():
    for  value in item.values():
          print(value) 
          
for item in dict_data.values():
    print(items[‘money’])

WHILE LOOPS : 

EXAMPLE1: 
x =0 
while x < 10:
       print( f”It’s working -> {x}’)
       if x == 4:
          break
       x+=1
age  = input(“what is your age”)
print(f”your age is [age}”)
 
 --------
EXAMPLE2:
user_prompt = True
while user_prompt: 
        age = input(“What is your age”)
        if age.isdigit():
           user_propt = False
        else:
           print(“Please provide your answer in digits”)

print(f” your age is {age}”)



FUNCTIONS : 
functions will return something - a good function returns something.
functions are all about reusability

EXAMPLES : 
def print_something(print_string):
    print(print_string)

print_something(“Hello world”)

def greeting(name):
      print(“Hello my name is: “+ name)

greeting(“Susan”)

def addition(int1,int2):
       return  int1+int2

addition(2,3)


WE CAN ALSO HAVE MULTIPLE PARAMETERS: 

def multi_args(*multiargs):
     for arg in multiargs: 
         print(arg) 
 multi_args(2,4,5,3,5,3,2,4,5)
 
 def greeting(name: str):
      print(“Hello my name is:”+ name) 

def division(demo: int, num: int) -> float:
     return demo /num


def substraction(int1: int = 5,int2: int = 2 ) -> int:
      return int1-int2


a: int = 10
b: int = 7

print(subtraction(10,7))


OOP:it allows us to have reusable code.

It employs good practice by allowing us to represent things as objects.

class Dog: 
     animal_kind = “canine”
#class variable which returns an attribute of String
     def bark(self):
#a method not a function
          return “woof”

pet1 = Dog()

print(pet1.bark())
print(type(pet1))
print(pet1.bark())

class Dog: 
     
     def __init__(self,name,color):
           self.animal_kind = “canine”
           self.name = name
           self.color = color
           self.bark()
     def bark(self):
             return “woof”

fido = Dog(“Fido”,”red”)


#class variable which returns an attribute of String
#a method not a function
     class Dog:
    def __init__(self, name, color):
        self.animal_kind = "canine"
        self.name = name
        self.color = color
        self.bark()
    def __repr__(self):
        print(f"The object is {self.name} ")
    def bark(self):
        return "woof"

fido = Dog("Fido", "red")
print(fido)

class Example:
      def __init__(self):
        self.example_this = "this can be accesed easily"
      def get_this(self):
          return self.example_this
      def set_this(self,new_example):
          self.example_this = new_example
          

x = Example()
print(x.example_this)

-----

FORMATTING THE DATE : 

class Location: 
       def __init__(self,latitude,longitude):
            self.latitude = latitude
            self.longitude = longitude
       def __repr__(self):
             return f”Location  latitude + {self.latitude} longitude {self.longitude})”
        def __str__(self):
              return f” ( {self.latitude}, {self.longitude}”
 n= 0.04837


print(f”Fixed Point: {n:f}”)
print(f”Exponential notation {n:e}”)


bham_academy = Location(52.4888647,-1887249)

print(bham_academy)


LAMBDA FUNCTIONS : 

def add(num1,num2): 
     return num1+ num2

addition = lamb num1,num2:num1+num2 


print(add(2,2))

print(addition(2,2,))

savings  =[234,555,674,78]
bonus = list(map(lambda x: x*1.1,savings)

print(bonus)



UNIT TESTING : 
Unit testing 

— the code runs that is not what is expected
helping us validate the logic of the implementation 

— run the test and watch it fail 

run you test suit .repreat steps 3 and 4 until all tests pass.

from simple_calc import SimpleCalc
import unittest


class Calctest(unites.TestCase):
     calc = SimpleCalc()
     def  test_add(self):
            self.assertEqual(self.calc.add(2,4),6)

    def  test_add(self):
            self.assertEqual(self.calc.subtract(2,2),0)
  
    def  test_add(self):
            self.assertEqual(self.calc.multiply(2,4),8)
   def  test_add(self):
            self.assertEqual(self.calc.divide(4,4),1)


class SimpleCalc: 
        def add(self, num1,num2):
              return num1 + num2

        def substract(self,num1,num2):
             return num1 -num2
       
       def divide(self,num1,num2):
            return num1*num2
   
       def multiply(self,num1,num2):
            return num1/num2












—————





































