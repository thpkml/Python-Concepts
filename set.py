# Sets are data structures
# They hold no duplicate elements
# They have no order

numbers = {1, 2, 3, 4, 5}
numbers1 = {1, 3, 5, 7, 9}
words = set(["apple", "boy", "cat"])
letters = {"a", "b", "c", "d", "e", "f"}

# function 'in/not in'

print(2 in numbers)
print(5 not in numbers)
print("boy" in words)
print("dog" in words)
print("b" in letters)
print("g" in letters)


# function len (for the length of set)

print(len(numbers))
print(len(words))
print(len(letters))


# function add, remove and pop
# pop removes a random element

letters.add(6)
print(letters)

letters.remove("a")
print(letters)

letters.pop()
print(letters)


# Set Operations: Union (|), Intersection (&), Difference(-), Symmetric Difference (^)

print(numbers | words)
print(numbers | numbers1)
print(numbers & numbers1)
print(numbers1 - numbers)
print(numbers - numbers1)
print(numbers ^ numbers1)
print(numbers1 ^ numbers) # same as the one above
