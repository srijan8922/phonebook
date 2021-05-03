from tkinter import *
class Application(object):
    def __init__(self,master):
        self.master = master

        self.top = Frame(master, height= 150, bg= 'yellow')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height= 500, bg= '#14075c')
        self.bottom.pack(fill=X)


def main():
    root = Tk()
    app = Application(root)

    root.title("Phonebook app")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()

