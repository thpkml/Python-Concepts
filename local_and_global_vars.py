total = 10; #this is the global variable
def sum(arg1, arg2):
    total = arg1 + arg2; #this 'total' is a local variable inside the function 'sum'
    print("inside the function local total:", total)
    return total;

#now you cn call the sum function
sum(10, 20);
print("outside the function global total:", total)
