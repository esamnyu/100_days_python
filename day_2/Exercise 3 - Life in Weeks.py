# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lifespan = 90

remaining_time = 90 - int(age)
months = 12*remaining_time
weeks = 52*remaining_time
days = 365*remaining_time
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

