'''You are to create a program to display a student's grades. Their grades will be listed
with each subject, e.g.:
				Joe Bloggs
		Computer Systems			Pass
		Networking Concepts			Merit
		Programming Concepts		Distinction
		Website Design			Pass
		Personal Skills Development		Pass
		Object Oriented Design		Merit
		Database Analysis and Design	Distinction
		Object Oriented Programming	Distinction

Write a program to accept a student's name and grade for each subject then display the
resulting transcript similar to above.
Further, apply loop control structure to continue the program until user 
enters ‘exit’.'''
import time
name = input("Enter student's full name: ")
time.sleep(1)
print ("Enter", name,"'s marks for the following subjects:")

# here we are assigning short names for the subjects for later purposes.
sub1 = "1. Computer Systems: "
sub2 = "2. Networking Concepts: "
sub3 = "3. Programming Concepts: "
sub4 = "4. Website Design: "
sub5 = "5. Personal Skills Development: "
sub6 = "6. Object Oriented Design: "
sub7 = "7. Database Analysis and Design: "
sub8 = "8. Object Oriented Programming: "

# assigning variables for grades.
a = "Distinction"
b = "Merit"
c = "Pass"
d = "Fail"
e = "Invalid entry ! Try again."


# THIS IS THE BEGINNING OF THE COMMANDS
while True:
    print("Or enter '-1' to exit!")
 
		#list the name of the subject and ask to enter the marks.
    mark1 = int(input(sub1))

    if mark1 == -1: #this will break the loop before it begins and asks for further entries.
        break
    
    mark2 = int(input(sub2))
    mark3 = int(input(sub3))
    mark4 = int(input(sub4))
    mark5 = int(input(sub5))
    mark6 = int(input(sub6))
    mark7 = int(input(sub7))
    mark8 = int(input(sub8))

    # the following is the condition for grades based on marks scored.    
    if mark1 in range (75,101):
        grade1 = a
    elif mark1 in range (60,75):
        grade1 = b
    elif mark1 in range (40,60):
        grade1 = c
    elif mark1 > 100:
        grade1 = e
    elif mark1 < 0:
        grade1 = e
    else:
        grade1 = d

    # repeat condition for sub2.

    if mark2 in range (75,101):
        grade2 = a
    elif mark2 in range (60,75):
        grade2 = b
    elif mark2 in range (40,60):
        grade2 = c
    elif mark2 > 100:
        grade2 = e
    elif mark2 < 0:
        grade2 = e
    else:
        grade2 = d

    # repeat condition for sub3.

    if mark3 in range (75,101):
        grade3 = a
    elif mark3 in range (60,75):
        grade3 = b
    elif mark3 in range (40,60):
        grade3 = c
    elif mark3 > 100:
        grade3 = e
    elif mark3 < 0:
        grade3 = e
    else:
        grade3 = d

    # repeat condition for sub4.

    if mark4 in range (75,101):
        grade4 = a
    elif mark4 in range (60,75):
        grade4 = b
    elif mark4 in range (40,60):
        grade4 = c
    elif mark4 > 100:
        grade4 = e
    elif mark4 < 0:
        grade4 = e
    else:
        grade4 = d

    # repeat condition for sub5.

    if mark5 in range (75,101):
        grade5 = a
    elif mark5 in range (60,75):
        grade5 = b
    elif mark5 in range (40,60):
        grade5 = c
    elif mark5 > 100:
        grade5 = e
    elif mark5 < 0:
        grade5 = e
    else:
        grade5 = d

    # repeat condition for sub6.

    if mark6 in range (75,101):
        grade6 = a
    elif mark6 in range (60,75):
        grade6 = b
    elif mark6 in range (40,60):
        grade6 = c
    elif mark6 > 100:
        grade6 = e
    elif mark6 < 0:
        grade6 = e
    else:
        grade6 = d

    # repeat condition for sub7.

    if mark7 in range (75,101):
        grade7 = a
    elif mark7 in range (60,75):
        grade7 = b
    elif mark7 in range (40,60):
        grade7 = c
    elif mark7 > 100:
        grade7 = e
    elif mark7 < 0:
        grade7 = e
    else:
        grade7 = d

    # repeat condition for sub8.

    if mark8 in range (75,101):
        grade8 = a
    elif mark8 in range (60,75):
        grade8 = b
    elif mark8 in range (40,60):
        grade8 = c
    elif mark8 > 100:
        grade8 = e
    elif mark8 < 0:
        grade8 = e
    else:
        grade8 = d
    # THIS NEEDS TO BE FIXED !!!!!!
    #if mark1 == -1:
        #break
    #else: 
    time.sleep(1)

    print ("=================================================================")
    print ("       ","Following are", name,"'s grades in all subjects:")
    print ("=================================================================")
    time.sleep(0.5)
    print ("       ",sub1, "            ",mark1, "       ", grade1)
    time.sleep(0.5)
    print ("       ",sub2, "         ",mark2, "       ", grade2)
    time.sleep(0.5)
    print ("       ",sub3, "        ",mark3, "       ", grade3)
    time.sleep(0.5)
    print ("       ",sub4, "              ",mark4, "       ", grade4)
    time.sleep(0.5)
    print ("       ",sub5, " ",mark5, "       ", grade5)
    time.sleep(0.5)
    print ("       ",sub6, "      ",mark6, "       ", grade6)
    time.sleep(0.5)
    print ("       ",sub7, "",mark7, "       ", grade7)
    time.sleep(0.5)
    print ("       ",sub8, " ",mark8, "       ", grade8)
    print ("=================================================================")

    total = mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7 + mark8
    average = int(total/8)
    if average in range (75,101):
        avGrade = a
    elif average in range (60,75):
        avGrade = b
    elif average in range (40,60):
        avGrade = c
    elif average > 100:
        avGrade = e
    elif average < 0:
        avGrade = e
    else:
        avGrade = d
    time.sleep(0.5)
    print ("=======================================")
    print("Your Total score out of 800 is:", total)
    print ("=======================================")
    time.sleep(0.5)
    print ("============================================")
    print("Your average score is:", round(average,2), ", which is a", avGrade)
    print ("============================================")
    time.sleep(0.5)
    if avGrade == a:
        print("Congratulations!!, wish you all the best.")
        print("Enter", name,"'s marks again.")
    elif avGrade == b:
        print("Congratulations!!, wish you all the best.")
        print("Enter", name,"'s marks again.")
    elif avGrade == c:
        print("You've passed the exam, but you can do better.")
        print("Enter", name,"'s marks again.")
    elif avGrade == d:
        print("Please try harder next time. All the best.")
        print("Enter", name,"'s marks again.")
    else:
        print("Invalid entry. Try again!")


    
   
