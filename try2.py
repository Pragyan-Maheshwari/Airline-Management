import tkinter as tk

def change_color(color):
    "Change color of widgets."
    window.config(bg=color)
    user_label.config(bg=color)
    pass_label.config(bg=color)
    user_entry.config(highlightbackground=color)
    pass_entry.config(highlightbackground=color)
    user_entry.config(fg=color, insertbackground=color)
    pass_entry.config(fg=color, insertbackground=color)

window = tk.Tk()
# username
user_label = tk.Label(window, text='Username')
user_entry = tk.Entry(window, bg='black')
# password
pass_label = tk.Label(window, text='Password')
pass_entry = tk.Entry(window, bg='black')
user_label.grid(row=0, column=0)
user_entry.grid(row=0, column=1)
pass_label.grid(row=1, column=0)
pass_entry.grid(row=1, column=1)
# changes color
user_entry.bind("<1>", lambda _: change_color("#99c9ff"))
pass_entry.bind("<1>", lambda _: change_color("#ffaf99"))
window.mainloop()
