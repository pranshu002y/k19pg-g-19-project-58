from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as tkMessageBox


#front end
first= Tk()
first.title("CONTACT LIST INTERFACE")
first.geometry('500x600')
first.resizable(0,0)
first.config(bg="#00ffff")


#VARIABLES USED IN THE CODE
NAME = StringVar()
EMAIL = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()

#Various functions used

#FUNCTION FOR CREATING THE DATABASE
def create_database():
    key = sqlite3.connect("Ravi.db")
    pointer = key.cursor()
    pointer.execute("CREATE TABLE IF NOT EXISTS 'contact' (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, NAME TEXT, EMAIL TEXT, ADDRESS TEXT, CONTACT TEXT)")
    pointer.execute("SELECT * FROM 'contact' ORDER BY 'NAME' ASC")
    read = pointer.fetchall()
    for i in read:
        tree.insert('', 'end', values=(i))
    pointer.close()
    key.close()

#FUNCTION FOR ADDING NEW DATA TO THE DATABASE

def put_data():
    if  NAME.get() == "" or EMAIL.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Fill Up The Required Field', icon="warning")
    else:
        key = sqlite3.connect("Ravi.db")
        pointer = key.cursor()
        pointer.execute("INSERT INTO 'contact' (NAME, EMAIL, ADDRESS, CONTACT ) VALUES(?, ?, ?, ?)", (str(NAME.get()), str(EMAIL.get()), str(ADDRESS.get()), str(CONTACT.get())))
        key.commit()
        pointer.execute("SELECT * FROM 'contact' ORDER BY 'NAME' ASC")
        read = pointer.fetchall()
        pointer.close()
        key.close()
        NAME.set("")
        EMAIL.set("")
        ADDRESS.set("")
        CONTACT.set("")


#FUNCTION FOR CREATING NEW CONTACT WINDOW
def new_contact():
    global add_mem
    NAME.set("")
    EMAIL.set("")
    ADDRESS.set("")
    CONTACT.set("")
    add_mem = Toplevel()
    add_mem.title("New Contact")
    add_mem.resizable(0, 0)
    add_mem.geometry('400x340')
   
    
    #FRAMES USED FOR NEW CONTACT WINDOW
    FormTitle = Frame(add_mem)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(add_mem)
    ContactForm.pack(side=TOP, pady=20)
    
    #LABELS USED FOR NEW CONTACT WINDOW
    heading = Label(FormTitle, text="ENTER THE DETAILS", font=('arial', 16), bg="cyan", bd=15, width = 280)
    heading.pack(fill=X)
    new_name = Label(ContactForm, text="NAME", font=('arial', 14), bd=10)
    new_name.grid(row=0, sticky=W)
    new_email = Label(ContactForm, text="E-MAIL", font=('arial', 14), bd=10)
    new_email.grid(row=1, sticky=W)
    new_address = Label(ContactForm, text="ADDRESS", font=('arial', 14), bd=10)
    new_address.grid(row=2, sticky=W)
    new_contact = Label(ContactForm, text="CONTACT", font=('arial', 14), bd=10)
    new_contact.grid(row=3, sticky=W)

    #ENTRY USED FOR NEW CONTACT FORM
    in_name = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
    in_name.grid(row=0, column=1)
    in_email = Entry(ContactForm, textvariable=EMAIL, font=('arial', 14))
    in_email.grid(row=1, column=1)
    in_address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    in_address.grid(row=2, column=1)
    in_contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    in_contact.grid(row=3, column=1)
    

    #BUTTON USED IN THE NEW CONTACT WINDOW
    finalize = Button(ContactForm, text="DONE",bd=10,bg='brown', width=50, command=put_data)
    finalize.grid(row=4, columnspan=2, pady=10)



#heading title
heading= Label(first, text="CONTACT LIST MENU", bd= '15', font=('forte',18),
               bg='pink',height=1,
               width=25).place(x=80,y=50)
#buttons
b1 = Button(first,bg='black',fg='cyan', font=('algerian',14),
            text = 'ADD NEW CONTACT',bd = '15', command = new_contact,
            height=2,width=20).place(x=120,y=200)
b2 = Button(first,bg='black',fg='cyan', font=('algerian',14),
            text = 'VEIW ALL CONTACT',bd = '15', command= NONE,
            height=2,width=20).place(x=120,y=300)
b3 = Button(first,bg='black',fg='cyan', font=('algerian',14),
            text = 'EXIT',bd = '15', command= first.destroy,
            height=2,width=20).place(x=120,y=400)
first.mainloop()
