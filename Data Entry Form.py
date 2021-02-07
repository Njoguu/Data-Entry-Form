from tkinter import *

from tkinter.ttk import Combobox


class Registration:

    def __init__(self,reg):
        # Labels for the Entry form
        self.lbl1 = Label(reg, text="First Name:", font=("Arial Black", 8))
        self.lbl2 = Label(reg, text="Second Name:", font=("Arial Black", 8))
        self.lbl3 = Label(reg, text="Age:", font=("Arial Black", 8))
        self.lbl4 = Label(reg, text="Adm Number:", font=("Arial Black", 8))
        # label for DropDown
        self.lbl5 = Label(reg, text="Faculty / College: ", font=("Arial Black", 8)).grid(column=0,
                                                     row=5, padx=150, pady=200)

        # Combobox creation
        n = StringVar()
        facultychoosen = self.lbl5 = Combobox(reg, width=27, textvariable=n)

        # Adding combobox drop down list
        facultychoosen['values'] = (' Business',
                                  ' Technology',
                                  ' Ed. & Arts',
                                  )

        facultychoosen.grid(column=1, row=5,)
        facultychoosen.current()

        self.entr1 = Entry(fg='black', bg='white')
        self.entr2 = Entry(fg='black', bg='white')
        self.entr3 = Entry(fg='black', bg='white')
        self.entr4 = Entry(fg='black', bg='white')
        self.lbl1.place(x=150, y=50)
        self.entr1.place(x=250, y=50)
        self.lbl2.place(x=450, y=50)
        self.entr2.place(x=550, y=50)
        self.lbl3.place(x=150, y=100)
        self.entr3.place(x=250, y=100)
        self.lbl4.place(x=150, y=150)
        self.entr4.place(x=250, y=150)














window=Tk()
window.title("Student Registration")
mywin=Registration(window)
lbl=Label(window, text="STUDENT REGISTRATION", fg='black', font=("Arial Black", 16))
lbl.place(x=0,y=0)
window.geometry("900x700+10+20")
window.mainloop()

