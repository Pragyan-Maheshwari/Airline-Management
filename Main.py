from tkinter import *
import tkinter as tink
from PIL import ImageTk,Image
import tkinter.ttk as ttk
import json
from Admin_Interface import Admin
from Passanger_Interface import PassangerFunction
  
window = tink.Tk()
window.geometry("1300x700")
window.title("Airline Booking")

frame1=Frame(window,width= 13000000,height=700000000)
frame1.pack() 
frame1.place(anchor="s",relx=0.5,rely=1.0)
img = ImageTk.PhotoImage(Image.open("image for front page.jpg"))
mylable = Label(frame1,image = img)
mylable.pack()

Adminbutton = tink.Button(text="Admin",font=("Great Vibes",20,"italic"),height=2,width=10,command=Admin)
Adminbutton.pack(side="top",ipadx=15,ipady=3)

Passangerbutton = tink.Button(text="Passanger",font=("Great Vibes",20,"italic"),height=2,width=10,command=PassangerFunction)
Passangerbutton.pack(side="top",ipadx=15,ipady=3)

window.mainloop()