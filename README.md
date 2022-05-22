# DevOps

PYTHON programming language 

What is a variable : it’s a box that holds information 

a = 1
b = 2
c = 3.5
hi = “Hello world”

origin = “http://github.com”

print(hi)

I can use this variable multiple times in repetition.

Python is a dynamic language.

it automatically figures out the type.

We can force things to be of a certain type : 
b = int(b) 

print(type(hi))
we can always validate what the type is with the type method.

We can also overwrite the value of a variable
a += 5

Programming is sequential —line by line : top to bottom.


When programming we need to remember how things interact.

Capturing user’s input : 
a = input(“Please enter the value of a”)
If you want to input staff during runtime ,input is very strong.

EXERCISE1 : 
name = input("Please enter your name")
age = int(input("Please enter your age"))
date_of_birth = input("Enter date of birth")
location = input("Enter your location")
weather = input("Enter the weather")
hobby = input("Which is your hobby?")
job = input("Please enter your job details")

salary = input(f"What is your salary after tax?:")
print(f"My name is {name}, I am {age}, my date of birth is {date_of_birth},I live in {location},"
      f"\n and here the weather is {weather}"
      f"My hobby is {hobby} and my job is {job} and my salary is {salary}")
a = 1
b = 2
c = 3
a = a +b

# check  a == b
# assignment a = b

a!=b
a<=b
a>=b
a==b

We can do maths in Python .

number1 = 5 # it’s a int
number2 = 5.5 # float
number3 = 45.j # complex type


number4 = 3e +26J
Long numbers no longer exist in Python.

float_num = 1.365
int_num = 5
print(float_num + int_num) 
#il will combine a float with an int to make another float

STRINGS : 
Because Python is flexible we can use ‘ ‘ or “ “ .

single_quotes = ‘This works’
double_quotes = “This also works”

a_string = “Wow  \”I don’t like this\” ”


We can also do slicing 
Hw = “Hello world”
print(Hw[7:]) # World
print(Hw[-5:]) #World
print(Hw[:5]) # Hello
print(Hw[0:5]) # Hello

print(len(Hw))
# calculates the length of the string

METHODS : 

white_space = “lots of white space at the end           “

print(white_space.strip())
#the string will not have the white space anymore outside of it

example_text = “here is some text “
print(example_text.count(‘text’))


#counts how many times text appears in the sentence
print(example_text.count(‘text’))
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace(“with”, ”,”)


CONCATENATION : 

a = “here”
b = “more”
c = “much more”
print( a + b+ c) 

RESULT : heremuchmuchmore

x = 2
y = 5.4
z = “  there is a number 25.4 unless we put a space in !”


print(x + y + z ) 

#error we can’t add ints/ floats and strings 


int_string = “6”
print(int(int_string))
print(type(int(int_string))

a = “2”
b = “4”
print(int(a) +int(b) )

F STRINGS /replaces the casting : 

name = “lassie”
years = 7
height_cm = 60.2
print(f “ {name} is {years} old and {height_cm} cm tall.”)

We can also do expressions evaluations in the F-strings:
name = “Snoopy”
years = 52

print(f”{name.upper()} is {years + 7 } years old in dog “)

pi = 3.1415926

print(f”PI to 3 decimal place: {pi: .3f} “) 
# Pi to 3 decimal place

score = 16

max_score = 26

print(f” you scored {score/max_score}”)
# result 0.6153…
print(f” you scored {score/max_score: %}”)
#result  61.53…%

print(f” you scored {score/max_score: .2%”)
#result : 61.53%

print(f” you scored {score/max_score: .0%}”)
# result rounding up 62 %

a = True 

b = False 

print(a == b) 

print( a >= b) 
print(a!=b)

print(True and False)

print(True or False)

print(False and True) 

hi = “Hello world”

print(hi.isalpha())

print(hi.islower())

print(hi.endswith(“!”))

print(hi.startswith(“H”))

x = 0
y = 10 

print(bool(x))

True can be anything which is not 0.

print(bool(None))
# false 

checking if the boolean operators work 
x = None 
# we can set something to be completely empty

print(x == False)
# false

print(x ==True) 
# false
shopping_list = [‘eggs’,’bread’,’bananas’,’biscuits’,’milk]


shopping_list.apped(‘carrots)

print(shopping_list)

shopping_list.remove(“bread”)

shopping_list.pop()

Lists can contain any number of data types ; 

mixture = [1,2,3,”one”,”three”]

We can do slicing as well 

print(mixture[1:3])
print(mixtture[-2::]
print(mixture[::2])


TUPLES — they are immutable 

foods = (“bread”,”milk”,”eggs”)
foods.count(“eggs”)

# the only methods available are : index and count in tuples

DICTIONARIES : 

student_1 = {
 “name”: “Suzan”,
 “stream”: “teach”,
“completed_lessons: 4,
“courses”: [“SQL”,”Python,”C”]
}

SETS : 
car_parts = {“wheels”,”doors”,”Exhaust”}
print(car_parts)

car_parts.add(“windows”)
print(car_parts)

# adds items RANDOMY
#it has all the usual methods

cars_parts.discard(“doors”)




      
