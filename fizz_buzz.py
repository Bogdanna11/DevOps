i = 1
new_list =[]
while i <=100:
    new_list.append(i)
    i+=1

for i in range(len(new_list)):
    if (new_list[i]%15)==0:
        new_list[i] = 'Fizz-Buzz'
    elif(new_list[i]%5)==0:
        new_list[i] =  'Fizz'
    elif(new_list[i]%3)==0:
        new_list[i] = "Buzz"
print(new_list)
