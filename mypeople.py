from tkinter import *
import sqlite3
from addpeople import AddPeople
from updatepeople import Update
from display import Display
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()

class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("My People")
        self.resizable(FALSE, FALSE)

        self.top = Frame(self, height=150, bg='red')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='orange')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='My people', font='arial 15 bold', bg='red', fg='orange')
        self.heading.place(x=260, y=50)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox = Listbox(self.bottom, width=50, height=35)
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        count = 0
        persons = cur.execute("select * from 'address book'").fetchall()
        print(persons)
        for person in persons:
            self.listbox.insert(count, str(person[0])+ "."+person[1]+ " " +person[2])
            count += 1

        self.scroll.grid(row=1, column=1, sticky=N+S)

        btnadd = Button(self.bottom, text="Add", width="12", font="Sans 12 bold", command=self.add_people)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnupdate = Button(self.bottom, text="Update", width="12", font="Sans 12 bold", command=self.update_function)
        btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndisplay = Button(self.bottom, text="Display", width="12", font="Sans 12 bold", command=self.display_people)
        btndisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width="12", font="Sans 12 bold", command= self.delete_person)
        btndelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query = "delete from 'address book' where person_id = {}".format(person_id)
        answer = messagebox.askquestion("warning", "are you sure you wanna delete")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("success", "Deleted")
                self.destroy()

            except Exception as e:
                messagebox.showinfo("Info", str(e))

    def add_people(self):
        add = AddPeople()
        self.destroy()

    def update_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        updatepage = Update(person_id)

    def display_people(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        displaypage = Display(person_id)











