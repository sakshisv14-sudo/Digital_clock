import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 50), background="black", foreground="cyan")
label.pack(anchor='center')

def update_time():
    time_string = strftime("%H:%M:%S")
    label.config(text=time_string)
    label.after(1000, update_time)

update_time()
root.mainloop()
