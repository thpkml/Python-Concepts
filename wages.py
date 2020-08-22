hours = eval(input("Enter hours worked:"))
rate = eval(input("Enter rate:"))
wage = hours*rate

if hours > 0 and rate > 0:
    print("Your wage for", hours, "hours is:", wage)
elif hours == 0 or rate == 0:
        print("Your wage for", hours, "hours is:", wage)
else:
    print("That can't be right mate!")
