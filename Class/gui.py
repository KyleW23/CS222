import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.geometry('500x300')
hello = tk.Label(text="Hello CS 222", foreground="blue")
hello.grid(column=0, row=0)
# hello.pack()
clickMe = tk.Button(text="Click me", width=10, height=3)
clickMe.grid(column=1, row=1)
# clickMe.pack()

window.mainloop()
