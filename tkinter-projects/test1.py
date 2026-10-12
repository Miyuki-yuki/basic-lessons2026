from tkinter import *
window = Tk()
window.title("Hello")
Label(text="It works!").pack()
Button(text="Click me", command=lambda: print("clicked!")).pack()
window.mainloop()