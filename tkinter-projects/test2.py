from tkinter import *
from tkinter import messagebox
from playsound import playsound

GREEN = "#3a6fb8"
RED = "#e7305b"
YELLOW = "#c7e0ff"
FONT = "Courier"
timer = None


def reset_timer():
    global timer
    if timer:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)


def start_timer():
    global timer
    if timer:
        window.after_cancel(timer)
        timer = None
    try:
        mins = int(minutes_entry.get())
        if mins <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(title="Oops", message="Minutes needs a number, like 25.")
        return
    title_label.config(text="Focus", fg=GREEN)
    count_down(mins * 60)


def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        title_label.config(text="Done!", fg=RED)
        playsound("timer-1.mp3")


window = Tk()
window.title("Focus Timer")
window.config(padx=40, pady=30, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT, 50))
title_label.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="apple.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold"))
canvas.grid(row=1, column=0, columnspan=2)

Label(text="Minutes", bg=YELLOW).grid(row=2, column=0, columnspan=2)
minutes_entry = Entry(width=4)
minutes_entry.insert(0, "25")
minutes_entry.grid(row=3, column=0, columnspan=2)

Button(text="Start", command=start_timer).grid(row=4, column=0, pady=10)
Button(text="Reset", command=reset_timer).grid(row=4, column=1, pady=10)

window.mainloop()