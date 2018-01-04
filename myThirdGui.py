from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.update_text()

    def create_widget(self):
        Label(self,
              text = "Wybierz swoje ulubione gatunki filmów."
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
             text="Zaznacz wszystkie, które chciałbyś wybrać: "
             ).grid(row=1, column=0, sticky=W)

        self.favorite = StringVar()
        self.favorite.set(" ")
        Radiobutton(self,
                    text = "komedia",
                    variable = self.favorite,
                    value = "komedia",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)


        Radiobutton(self,
                    text="dramat",
                    variable=self.favorite,
                    value="dramat",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)


        Radiobutton(self,
                    text="romans",
                    variable=self.favorite,
                    value="romans",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        self.results_txt = Text(self, width = 40, height = 15, wrap = WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        message = "Twoim ulubionym gatunkiem filmowym jest: "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

root = Tk()
root.title("Wybór filmów")
root.geometry("300x300")

app = Application(root)

root.mainloop()
