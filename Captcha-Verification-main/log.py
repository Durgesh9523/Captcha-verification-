from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        username=[]
        pwd=[]
        for row in c.execute("Select * from data"):
            username.append(str(row[2]))
            pwd.append(str(row[4]))
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname =str(reg_no.get())
    upwd = str(pwd_tf.get())
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname in username and upwd in pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)
root.geometry("500x500")
Label(
    root,
    text="Enter Email", 
    bg='#CCCCCC',
    font=("bold",20)).place(x=50,y=60)

Label(
    root, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=("bold",20)
    ).place(x=50,y=190)

reg_no = Entry(
   root)
reg_no.place(x=240,y=60)
pwd_tf = Entry(
   root, 
    font=("bold",20),
    show='*'
    )
pwd_tf.place(x=240,y=190)
login_btn = Button(
    root, 
    width=15, 
    text='Login', 
    font=("bold",20), 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    ).place(x=240,y=240)
root.mainloop();