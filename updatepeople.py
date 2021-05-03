from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()

class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Update person")
        self.resizable(False, False)
        print("person id =", person_id)

        query = "select * from 'address book' where person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_email = result[5]
        person_phine = result[3]
        person_address = result[4]

        print("person name", person_name)
        print("person surname", person_surname)
        print("person email", person_email)
        print("person phone", person_phine)
        print("person address", person_address)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='grey')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Update people', font='arial 15 bold', bg='white', fg='grey')
        self.heading.place(x=260, y=50)

        self.label_name = Label(self.bottom, text="Name", font='arial 15 bold', fg="white", bg="grey")
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        self.label_surname = Label(self.bottom, text="Surname", font='arial 15 bold', fg="white", bg="grey")
        self.label_surname.place(x=49, y=100)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=150, y=100)

        self.label_email = Label(self.bottom, text="Email", font='arial 15 bold', fg="white", bg="grey")
        self.label_email.place(x=49, y=160)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=160)

        self.label_Phone_number = Label(self.bottom, text="Phone no.", font='arial 15 bold', fg="white", bg="grey")
        self.label_Phone_number.place(x=49, y=220)

        self.entry_Phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_Phone_number.insert(0, person_phine)
        self.entry_Phone_number.place(x=150, y=220)

        self.label_Address = Label(self.bottom, text="Address", font='arial 15 bold', fg="white", bg="grey")
        self.label_Address.place(x=49, y=280)

        self.entry_Address = Text(self.bottom, width=50, height=6)
        self.entry_Address.insert(1.0, person_address)
        self.entry_Address.place(x=150, y=280)

        button = Button(self.bottom, text="Update Person", font="arial 15 bold", fg="white", bg="black",
                        command=self.update_people)
        button.place(x=270, y=420)
    def update_people(self):
        id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_Phone_number.get()
        address = self.entry_Address.get(1.0, 'end-1c')

        query = "update 'address book' set person_name = '{}', person_surname = '{}', person_email = '{}', person_phine = {}, person_address = '{}' where person_id = {}".format(name, surname, email, phone, address, id)

        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Success", "contact updated")

        except Exception as e:
            print(e)


