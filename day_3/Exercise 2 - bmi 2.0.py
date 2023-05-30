# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def interpret_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        interpretation = "You are underweight"
    elif 25 > bmi > 18.5:
        interpretation = "You are overweight" 
    elif 30 > bmi > 25:
        interpretation = "You are slightly overweight"
    elif 35 > bmi > 30:
        interpretation = "You are obese"
    elif bmi > 35:
        interpretation = "You are clinically obese"
    return f"Your bmi is {bmi:.1f}, {interpretation}"
print(interpret_bmi(weight, height))

