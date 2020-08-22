# Recursion means self-referencing
# When a function calls itself.
# Example: a Factorial function


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(7))


# Example 2: Sum up to a number


def sum_to(x):
    if x == 0:
        return 0
    else:
        return x + sum_to(x - 1)


print(sum_to(40))


# Indirect Recursion: function1 calls function2 calls function1 and so on ..
# Example 3: Find odd/even


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x -1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(17))


# Example 4:

def fun(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fun(x - 1) + fun(x - 2)


print(fun(8))