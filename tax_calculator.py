import time
#input income
income = eval(input("Enter Income:"))
# if income > 100000
  # net = income * 0.5
if income > 100000:
  net = income * 0.5
# elif income > 35000
  # net = income * 0.6
elif income > 35000: 
  net = income * 0.6
#elif income > 11000
  # net = income * 0.8
elif income > 11000: 
  net = income * 0.8
# else
  # net = income
# print net
else: 
  net = income
  
print ("YEARLY")
print ("Your gross income is: £", income)
print ("Tax paid is: £", round((income - net), 2)) #This is to round the decimal
                                                   #value to two positions
print ("Your Take-home pay is: £", net)

time.sleep(2)

print ("===============================")

print ("MONTHLY")
print ("Your gross income is: £", round((income / 12), 2))
print ("Tax paid is: £", (income - net) / 12)
print ("Your Take-home pay is: £", net /12 )

time.sleep(2)

print ("===============================")

print ("WEEKLY")
print ("Your gross income is: £", income / 52)
print ("Tax paid is: £", round((income - net) / 52, 2))
print ("Your Take-home pay is: £", net / 52)
