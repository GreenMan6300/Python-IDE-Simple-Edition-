#This was coded on Python version 3.13
from tkinter import *
from tkinter import filedialog

print("Python IDE (Simple Edition)")
print("Created by GreenMan6300")
input("Press enter to start")
print("Starting..")

#Required to create window and set dimension and set the title of the Window
window = Tk()
window.geometry("460x460")
window.title("Python IDE (simple edition)")
#Changes the window appearance and icon
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background="#F0F0F0")

#The name of the Program Text!
label = Label(window, text="Python IDE (simple edition)")
label.config(font=("Arial", 20))
label.pack()

#Just to tell the user that there is no load or run
label = Label(window, text="Does not include it's own way to Run code or load .py")
label.config(font=("Arial", 10))
label.pack()

#The so annoying system i had to deal whit
def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".py",
                                    filetypes=[
                                        ("Python File"," .py")
                                    ])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

#Save Button
button = Button(text="Save",command=saveFile)
button.config(font=("Arial", 12))
button.config(bg="white", fg="black")
button.pack()

#Quit Button
def exit():
    window.destroy()
    print("Stopping..")

button = Button(text="Quit",command=exit)
button.config(font=("Arial", 12))
button.config(bg="white", fg="black")
button.pack()

#Text Editor
text = Text(window)
text.pack()

#Creates the Window
window.mainloop()