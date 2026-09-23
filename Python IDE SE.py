#This was coded on Python version 3.13.15 (Stable Releases)
#The python script has been tested whit a old version of Python that works on windows 7.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

print("Python IDE (Simple Edition)")
print("Version 0.1.5")
print("Created by GreenMan6300")
print("Update log:")
print("1: The Logo got the Font changed")
print("2: Window is now bigger")
print("3: Added the funny button")
print("4: A new iamge in the Image folder that is not used")
print("5: This script name is now Python IDE SE")
print("6: Save And Quit button now uses Arial Black")

#The Text editor Window
window = Tk()
window.geometry("750x550")
window.title("Python IDE (simple edition)")
#Changes the window appearance and icon
icon = PhotoImage(file='Images/icon.png')
name = PhotoImage(file='Images/name.png')
window.iconphoto(True, icon)
window.config(background="#A6C7D6")

#The name of the Program Text!
labellogo = Label(window, image=name)
labellogo.config(background="#A6C7D6")
labellogo.pack()

#Just to tell the user that there is no load or run
label = Label(window, text="Does not include it's own way to Run code or load .py")
label.config(font=("Arial", 10))
label.config(background="#A6C7D6")
label.pack()

#The so annoying system i had to deal whit for save button
def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".py",
                                    filetypes=[
                                        ("Python File"," .py")
                                    ])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.config(background="#A6C7D6")
    file.close()

#Save Button
button = Button(text="Save",command=saveFile)
button.config(font=("Arial Black", 11))
button.config(bg="#E5F8FF", fg="#1E2021")
button.config(activebackground="#1E2021")
button.config(activeforeground="#E5F8FF")
button.place(x=115, y=89)

#Quit Button
def exit():
    window.destroy()
    print("Session ended")

button = Button(text="Quit",command=exit)
button.config(font=("Arial Black", 11))
button.config(bg="#E5F8FF", fg="#1E2021")
button.config(activebackground="#1E2021")
button.config(activeforeground="#E5F8FF")
button.place(x=55, y=89)

#This is supposed to be a button that can load .py but im lazy to make it do something.
def load():
    messagebox.showinfo(title="Funny Button",message="Beep Boop!")

button = Button(text="Funny Button",command=load)
button.config(font=("Arial Black", 11))
button.config(bg="#E5F8FF", fg="#1E2021")
button.config(activebackground="#1E2021")
button.config(activeforeground="#E5F8FF")
button.place(x=180, y=89)

#Just to tell the user that there is no load or run
label = Label(window, text="")
label.config(font=("Arial", 20))
label.config(background="#A6C7D6")
label.pack()

#Text Editor
text = Text(window)
text.config(background="#EBF8FF")
text.pack()

#LavaMark or Watermark i forgot.
def greenmanwashere():
    print("GreenMan6300 Was here!")

button = Button(text="Made by GreenMan6300",command=greenmanwashere)
button.config(font=("Arial", 15))
button.config(bg="#B8DDED", fg="#22282B")
button.config(activebackground="#A6C7D6")
button.config(activeforeground="#39454A")
button.pack()

#Creates the Window
window.mainloop()

#GreenMan6300 was here