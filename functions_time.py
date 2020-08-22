import time
def goodmorning():
    print("Good morning")

def goodafternoon():
    print("Good afternoon")

def goodevening():
    print("Good evening")

print("Hello")
now = time.strftime("%H:%M:%S")
if now < "12:00:00":
    goodmorning()
elif now < "18:00:00":
    goodafternoon()
else:
    goodevening()
