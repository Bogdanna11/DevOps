def multi_args_addition(*multiargs):
    sum = 0
    for arg in multiargs:
        sum+=arg
    return sum
def substraction(x,y):
    return x-y
def multi_args_multiplication(*multiargs):
     result = 1
     for arg in multiargs:
         result *=arg
     return result
def division(x,y):
    return x/y
print(multi_args_addition(3,4,5,6,4))
print(multi_args_multiplication(1,2,2))
print(substraction(5,2))
