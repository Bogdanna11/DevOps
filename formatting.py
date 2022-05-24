check_flag = True
amount = int(input("please enter the amount of money"))
while check_flag:   
    if amount <= 0 : 
        amount = int(input("please enter a positive value "))
    elif amount>0:
        currency = "${:,.2f}".format(amount)
        print(currency)
        check_flag = False
        break
    else:
        amount = int(input("please enter a value"))
