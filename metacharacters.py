import re

# Raw strings: strings in which no character is escaped
rawstr = r"We\have\back?/slashes"
print(rawstr)

# Match Any character (Dot '.' notation)
pattern = r"app.e"
if re.match(pattern, "apple"):
    print("Match")

# Match Start (^) and End ($)
pattern1 = r"^Ka..l$"
if re.match(pattern1, "Kamal"):
    print("Matches Kamal")

if re.match(pattern1, "Kapal"):
    print("Matches Kapal")

# Character classes ["characters"]
pattern2 = r"[aeiou]"
if re.search(pattern2, "balls"):
    print("Vowel detected!")

if re.search(pattern2, "Grr!"):
    print("Vowels Detected!")
else:
    print("No Vowel!")

# Searching and Matching from a Range of characters
# Match any lowercase letter
pattern3 = r"[a-z]"
if re.search(pattern3, "Sup?"):
    print("Found one or more lowercase letter.")
else:
    print("no lowercase letter")

# Match: first lower, second upper, third digit
password = r"[a-z][A-Z][0-9]"
if re.search(password, "pW1"):
    print("Good Password")
else:
    print("Use lowercase, uppercase and numbers")

# Match PostCode Format
postcode = r"[A-Z][A-Z][0-9][ ][0-9][A-Z][A-Z]"
if re.search(postcode, "SW1 3FG"):
    print("Good PostCode")
else:
    print("Wrong Postcode format!")

# Invert the range e.g. [^A-Z]
benice = r"[^A-Z]"
if re.search(benice, "HELLO"):
    print("good boy")
else:
    print("be nice, no caps")

# Repititions of the previous thing

# '*' - zero or more repetitions
pattern4 = "sweet(jesus)*" # start with 'sweet' and have 0 or more 'jesus'
words = ['sweetjesus', 'sweet', 'jesus', 'sweetjesusjesus', 'effin joke!']
for i in range(len(words)):
    if re.match(pattern4, words[i]):
        print("Match sweet jesus!")
    else:
        print("Didn't find no sweet in jesus!")

# '+' one or more repetitions
pattern5 = "sweet(jesus)+" # start with 'sweet' and have 0 or more 'jesus'
words1 = ['sweetjesus', 'sweet', 'jesus', 'sweetjesusjesus', 'effin joke!']
for i in range(len(words1)):
    if re.match(pattern5, words1[i]):
        print("Match sweet jesus!")
    else:
        print("Didn't find no sweet in jesus!")

# '?' zero or one repetitions
colour = r"colo(u)?r" # find color or colour but nothing else

# {range} custom repetition range
zeros = r"0{3,5}$" # will accept 3 to 5 0's and no other char(coz $)
numbers = ['00', '000', '10000', '00000', '0005', '1000000']
for i in range(len(numbers)):
    if re.match(zeros, numbers[i]):
        print("You are in the range")
    else:
        print("Out of range!")