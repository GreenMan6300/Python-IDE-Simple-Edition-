#This was coded on Python version 3.13
from tkinter import *
from tkinter import filedialog

print("Python IDE (Simple Edition)")
print("Created by GreenMan6300")
print("Update log:")
print("1: new folder called Images")
print("2: removed press enter to start")
print("3: new icon and a new Logo")
print("4: text that has the name changed to the Logo")
print("5: Background and button and text is Blue")
print("6: save and quit isnt a sandwich anymore")

#Required to create window and set dimension and set the title of the Window
window = Tk()
window.geometry("500x500")
window.title("Python IDE (simple edition)")
#Changes the window appearance and icon
icon = PhotoImage(file='Images/icon.png')
logo = PhotoImage(file='Images/logo.png')
window.iconphoto(True, icon)
window.config(background="#A6C7D6")

#The name of the Program Text!
labellogo = Label(window, image=logo)
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
button.config(font=("Arial", 12))
button.config(bg="#CBEDFF", fg="#2F363B")
button.config(activebackground="#2F363B")
button.config(activeforeground="#CBEDFF")
button.place(x=200, y=89)

#Quit Button
def exit():
    window.destroy()
    print("Session ended")

button = Button(text="Quit",command=exit)
button.config(font=("Arial", 12))
button.config(bg="#CBEDFF", fg="#2F363B")
button.config(activebackground="#2F363B")
button.config(activeforeground="#CBEDFF")
button.place(x=250, y=89)

#Just to tell the user that there is no load or run
label = Label(window, text="")
label.config(font=("Arial", 18))
label.config(background="#A6C7D6")
label.pack()

#Text Editor
text = Text(window)
text.config(background="#A3DCFF")
text.pack()

#Creates the Window
window.mainloop()
