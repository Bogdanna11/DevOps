name = input("Enter your name please")
height = float(input("Enter your height please"))
favourite_color = input("Enter your favourite color")
secrete_spirit_animal = input("Enter your secret spirit animal ( don't press the tab bar before replying ) ")

print(f"Hello {name} and welcome to the secret forest, you have the height "
      f"of {height} which si just the right height to get in "
      f" add the color :{favourite_color} is a correct color.")
print(f"The first letter of the animal is : {secrete_spirit_animal[1]}")
print(f"The last letter of the animal is : {secrete_spirit_animal[-1]}")
print(len(secrete_spirit_animal))
flag = False
while not flag:
    guest_user = input("Please enter the name of the animal ( don't press the tab bar before replying )")
    if guest_user == secrete_spirit_animal:
        print("OMG you guessed it")
        flag = False
        break


