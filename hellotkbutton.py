import tkinter as tk
root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!", fg="red", bg="yellow", width=50)
w.pack()
def create_widgets():
    hi_there = tk.Button()
    hi_there["text"] = "Hello World\n(click me)"
    hi_there["command"] = say_hi
    hi_there.pack(side="top")

    quit = tk.Button( text="QUIT", fg="red", command=root.destroy)
    quit.pack(side="bottom")

def say_hi():
    print("hi there, everyone!")

create_widgets()
root.mainloop()
