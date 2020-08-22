import re

str = "If you want any assistance, kamal@gmail.com is my mail address. You can also use pauli@company.co.uk if I am not available."

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

# more accurate is the following pattern as the above pattern allows .@ as the email address name
pattern1 = r"(\w)+([\.-](\w+))*@(\w)+([\.-]\w)*(\.(\w+))"

# The regex used for email in the real world is much more complex. It is shown below:
pattern3 = "find here: emailregex.com"

match = re.search(pattern1, str)

if match:
    print("Email found: ")
    print(match.group())


# To extract multiple email addresses, use 'findall' instead of 'search'
# Remeber, 'findall' does not have the 'group()' method