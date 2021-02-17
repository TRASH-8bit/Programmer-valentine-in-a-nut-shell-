from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

#main window
root = Tk()
#resolution of the window
root.geometry("800x600")
#image path
path = "C:/Users/hp/Desktop/Phython code/KBCgame/heart.jpeg"

#defs for the click yes
def clickedyes():
    new= Toplevel()
    new.geometry("800x600")
    new.config(bg="yellow")
    path = "C:/Users/hp/Desktop/Phython code/KBCgame/fuck.png"
    my_pic = Image.open(path)
    resized_pic = my_pic.resize((400,400) , Image.ANTIALIAS)
    finalpic = ImageTk.PhotoImage(resized_pic)
    labelfucku = tk.Label(new, text="FUCK YOU" , font=("Arial",25), bg="yellow", fg="black")
    labelfucku.place(x=400,y=500, anchor="center")
    label = tk.Label(new, image = finalpic)
    label.pack()
    new.mainloop()

#def for the click no
def clickedno():
    new= Toplevel()
    new.geometry("800x600")
    new.config(bg="red")
    path = "C:/Users/hp/Desktop/Phython code/KBCgame/loser.png"
    my_pic = Image.open(path)
    resized_pic = my_pic.resize((400,400) , Image.ANTIALIAS)
    finalpic = ImageTk.PhotoImage(resized_pic)
    labelfucku = tk.Label(new, text="YOU ARE A LOSER" , font=("Arial",25), bg="red", fg="black")
    labelfucku.place(x=400,y=500, anchor="center")
    label = tk.Label(new, image = finalpic)
    label.pack()
    new.mainloop() 

# image resize 
my_pic = Image.open(path)
resized_pic = my_pic.resize((400,400) , Image.ANTIALIAS)
finalpic = ImageTk.PhotoImage(resized_pic)

# font and some other thing
label1=tk.Label(root, text="Will you be my vanlantine ?", font=("Arial", 25), bg="white", fg="black")
label1.place(x=400,y=500, anchor="center")

# button for yes 
button1=tk.Button(root, text="Yes", bg="black", fg="white", command=clickedyes)
button1.place(x=350,y=550, anchor="center")

# button for no
button2=tk.Button(root, text="NO", bg="black", fg="white", command=clickedno)
button2.place(x=450,y=550, anchor="center")

# label
label = tk.Label(root, image = finalpic)
label.pack()

root.mainloop()