
print("Welcome to the tip calculator!\n")
bill=input("What was the total bill?\n")
tip=input("How much tip would you like to give? 10, 12, or 15?\n")
people=input("How many people to split the bill?\n")
bill_float=float(bill)
tip_int=int(tip)
people_int=int(people)
tip_value=(bill_float*tip_int)/100
bill_total=bill_float+tip_value
bill_per_person=bill_total/people_int
rounded_bill=round(bill_per_person ,2)

print("Each person should pay: $" +str(rounded_bill))


