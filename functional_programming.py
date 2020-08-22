
''' Functional programming as the name suggests is programming around functions.
In the example below, we demonstrate that functions can become arguments themselves
of other higher order functions. '''
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))
