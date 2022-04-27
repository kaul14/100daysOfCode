print("Welcome to the tip calculator")

# now we will get the users to enter the values.
bill = input("What was the total bill? \n")
tip = input("How much tip would you like to give? 10, 12, or 15? \n")
num = input("How many people would you want to split the bill bw? \n")

# finding bill that each person has to pay.
bill_each_person = round((float(bill)*(int(tip)/100+1) )/ int(num),2)

print(f"Each person should pay {bill_each_person}")
