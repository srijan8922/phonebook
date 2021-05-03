from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add People")
        self.resizable(FALSE, FALSE)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='grey')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Add new people', font='arial 15 bold', bg='white', fg='grey')
        self.heading.place(x=260, y=50)

        self.label_name = Label(self.bottom, text="Name", font='arial 15 bold', fg="white", bg="grey")
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "Enter Name")
        self.entry_name.place(x=150, y=40)

        self.label_surname = Label(self.bottom, text="Surname", font='arial 15 bold', fg="white", bg="grey")
        self.label_surname.place(x=49, y=100)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "Enter Surname")
        self.entry_surname.place(x=150, y=100)

        self.label_email = Label(self.bottom, text="Email", font='arial 15 bold', fg="white", bg="grey")
        self.label_email.place(x=49, y=160)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "Enter Email")
        self.entry_email.place(x=150, y=160)

        self.label_Phone_number = Label(self.bottom, text="Phone no.", font='arial 15 bold', fg="white", bg="grey")
        self.label_Phone_number.place(x=49, y=220)

        self.entry_Phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_Phone_number.insert(0, "Enter Phone Number")
        self.entry_Phone_number.place(x=150, y=220)

        self.label_Address = Label(self.bottom, text="Address", font='arial 15 bold', fg="white", bg="grey")
        self.label_Address.place(x=49, y=280)

        self.entry_Address = Text(self.bottom, width=50, height=6)
        self.entry_Address.place(x=150, y=280)

        button = Button(self.bottom, text="Add Person", font="arial 15 bold", fg="white", bg="black", command=self.add_people)
        button.place(x=270, y=420)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_Phone_number.get()
        address = self.entry_Address.get(1.0, 'end-1c')

        if name and surname and email and phone and address != "":
            try:
                query ="insert into 'address book' (person_name, person_surname, person_email, person_phine, person_address)values(?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("success", "contact added")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "fill all the fields", icon='warning')
