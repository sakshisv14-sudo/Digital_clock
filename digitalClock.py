import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="black")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (400 // 2)
y = (screen_height // 2) - (200 // 2)
root.geometry(f"+{x}+{y}")

# Time Label
time_label = tk.Label(root, font=("Arial", 50, "bold"), bg="black", fg="cyan")
time_label.pack(pady=10)

# Date Label
date_label = tk.Label(root, font=("Arial", 20), bg="black", fg="lightgray")
date_label.pack()

def update_time():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)


update_time()
root.mainloop()
