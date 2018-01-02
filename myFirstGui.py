from tkinter import *
import tkinter.messagebox

def doNothing():
    print("Dupa!!!")

root = Tk()

tkinter.messagebox.showinfo("Window title", "Modern Galápagos tortoises can weigh up to 417 kg.")

answer =tkinter.messagebox.askquestion("Question 1", "Do you like dumplings?")

if answer == 'yes':
    print("I like you")
if answer == "no":
    print("skimp!")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_cascade(label="New Project", command=doNothing)
subMenu.add_cascade(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_cascade(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

toolbar = Frame(root, bg="green")

insertButt =  Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt =  Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()