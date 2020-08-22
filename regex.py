import re

pattern = r"dogs"
str = 'dogscatsgoats catsmiceratsdogs'

# Check for 'dogs' in the beginning
if re.match(pattern, str):
    print('Match')

# Check for 'dogs' anywhere
if re.search(pattern, str):
    print('Match')

# List all 'dogs' that match
print(re.findall(pattern, str))

# Find iterator for all matches of 'dogs'
print(re.finditer(pattern, str))

# Manipulating the result of Search
match = re.search(pattern, str)
if match:
    # group the Search result
    print(match.group())
    # find the span of Search result
    print(match.span())
    # find the start of Search result
    print(match.start())
    # find the end of Search result
    print(match.end())

# Substitute the pattern with replacement
repl = 'poodles'

newstr = re.sub(pattern, repl, str)
print(newstr)