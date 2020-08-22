# Special sequences are written as a Backslash (\) followed by another character

import re

pattern = r"(.+)\1" # any beginning - anything(.) one or more(+) - any end, repeat group 1

match = re.match(pattern, "11")
if match:
    print("Match 1!")
    print(match.groups())

match = re.match(pattern, "abc abc abc")
if match:
    print("Match 2")
    print(match.groups())

match = re.match(pattern, "abc def ghi")
if match:
    print("Match 3")
    print(match.groups())

match = re.match(pattern, "!-- !-- !--")
if match:
    print("Match 4")
    print(match.groups())

pattern1 = r"(.+)(.+)(.+)\2" # three groups each (anything once or more) - repeat group 2

match = re.match(pattern1, "aabbbc")
if match:
    print("Match 5")
    print(match.groups())