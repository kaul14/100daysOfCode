print("Welcome to the tip calculator")
bill = input("What was the total bill? \n")
tip = input("How much tip would you like to give? 10, 12, or 15? \n")
num = input("How many people would you want to split the bill bw? \n")

bill_each_person = round((float(bill)*(int(tip)/100+1) )/ int(num),2)

print(f"Each person should pay {bill_each_person}")
