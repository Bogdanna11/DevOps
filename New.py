user_prompt = True
my_username = "rusbogdana@yahoo.com"
password = "pass1"
while user_prompt:
    username = input("What is your username")
    if username.lower() == my_username:
        print("well done the username is true")
        user_password = input("please enter password")
        if user_password == password:
            print("Well done this is the correct password")
            user_prompt = False
            break
        else:
            print("Enter the password again")
    else:
        print("Please provide the correct username")
