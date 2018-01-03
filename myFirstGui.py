from tkinter import *
import tkinter.messagebox

def doNothing():
    print("I do nothing")

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Liczba kliknięć: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Liczba kliknięć: " + str(self.bttn_clicks)

from tkinter import *

root = Tk()
root.title("Licznik kliknięć")
root.geometry("225x100")


app = Application(root)

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


root.mainloop()