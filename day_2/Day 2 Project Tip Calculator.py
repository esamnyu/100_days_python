#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is your total bill?"))
num_people = int(input("How many people are you splitting your bill with?"))
tip_percentage = input("What is your tip?")
percentage = float("1."+ str(tip_percentage))

total_bill = round((bill/num_people) * percentage, 2)

print(total_bill)
