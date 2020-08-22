# Decorator functions help extend the functionality of other functions without them having to modify themselves

def decorator(func):
    def wrap():
        print("**************")
        func()
        print("**************")

    return wrap


def print_hello():
    print("HELLO WORLD!")


decorated = decorator(print_hello)
decorated()
