from tkinter import *
from tkinter import messagebox  # Importing messagebox module

root = Tk()
root.title("Yoga Reminder App")

def save_time():
    hour = hour_var.get()
    minute = minute_var.get()
    messagebox.showinfo("Yoga Reminder App", f"Your daily yoga routine has been set for {hour:02d}:{minute:02d}")

hour_var = IntVar()
minute_var = IntVar()

hour_label = Label(root, text="Hour:")
hour_label.pack()

hour_spinbox = Spinbox(root, from_=0, to=23, width=5, textvariable=hour_var)
hour_spinbox.pack()

minute_label = Label(root, text="Minute:")
minute_label.pack()

minute_spinbox = Spinbox(root, from_=0, to=59, width=5, textvariable=minute_var)
minute_spinbox.pack()

save_button = Button(root, text="Save", command=save_time)
save_button.pack()

root.mainloop()
