# The code on the previous file 'decorator.py' can be shortened the following way:
# Also, a single function can take multiple decorators


def decorator1(func):
    def wrap():
        print("*************")
        func()
        print("*************")

    return wrap


def decorator2(func):
    def wrap():
        print("================")
        func()
        print("================")

    return wrap

@decorator1
@decorator2
def print_hello():
    print("HELLO FRIEND!")


print_hello()
