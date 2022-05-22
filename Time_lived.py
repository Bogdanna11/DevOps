import datetime

date_of_birth = input("Please enter the exact date of birth ( for example:January 10 1985 )")
birthday = datetime.datetime.strptime(date_of_birth,'%B %d %Y')
today_date = datetime.datetime.today()
calc_time = (today_date - birthday).total_seconds()
print("You have been alive for",int(calc_time),"seconds")
time_minutes = calc_time/60
print("You have been alive for",int(time_minutes),"minutes")
time_hours = time_minutes/60
print("You have been alive for",int(time_hours),"hours")

