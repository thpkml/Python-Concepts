# Itertools is a module in Python Standard Library
# It has several useful functions to work with Iterables (e.g. string, list etc)
# functions include:
# count, cycle, repeat, accumulate, takewhile, product, permutations etc.

from itertools import count, cycle, repeat, accumulate, chain, takewhile, product, permutations

# count
for i in count(5, 4):
    print(i)
    if i >= 50:
        break

# cycle
i = 0
for c in cycle('Apple'):
    print(c)
    i += 1
    if i >= 5: break

# repeat
for i in repeat('Kamal', 3):
    print(i)
    print(list(i))

# accumulate
print(list(accumulate([1, 2, 3, 4, 5, 6, 7])))

# chain
print(list(chain('boy', 'girl')))

# takewhile
print(list(takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8])))

# product (Cartesian Product)
print(list(product([1, 2, 3], [1, 2, 3])))

# permutations
print(list(permutations('cat')))
