#The following code doesn't run as expected. This Python version doesn't
#recognize e.g. 'mark > 70'. 
mark = eval(input("Enter the mark:"))

if mark >=80:
    if mark > 90:
        print('A*')
    else:
        print("A")
            
elif mark >= 60:
    if mark > 70:
        print("B")
    else:
        print("C")
    
elif mark >= 40:
    if mark > 50:
        print("D")
    else:
        print("PASSED")
        
elif mark >= 0:
    print("FAILED")
else:
    print("Invalid entry!")
