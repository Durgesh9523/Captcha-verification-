from tkinter import *
from tkinter import messagebox
import sqlite3
''' root=Tk()
root.geometry("500x500")
def change_pass():
    old=str(reg_no.get())
    new=str(pwd_tf.get())
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("update data set password_p=:new_p where :old_p",{'new_p':new,'old_p':old})
        con.commit()
    except Exception as ep:
            messagebox.showerror('', ep)
Label(
    root,
    text="Enter old password", 
    bg='#CCCCCC',
    font=("bold",20)).place(x=50,y=60)

Label(
    root, 
    text="Enter new Password", 
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
    command=change_pass
    ).place(x=240,y=240)
root.mainloop()
         '''
def reset_pass():
    print("Hello")
win=Tk()
win.geometry("500x500")
label_0 =Label(win,text="Reset Your Password", width=20,font=("bold",20))
label_0.place(x=90,y=60)
label_1=Label(win,text="Old Password",width=20,font=("bold",15))
label_1.place(x=10,y=130)
old=Entry(win,show="*",width=20)
old.place(x=240,y=130)
label_2=Label(win,text="New Password",width=20,font=("bold",15))
label_2.place(x=10,y=200)
new=Entry(win,show="*",width=20)
new.place(x=240,y=200)
label_3=Label(win,text="Confirm Password",width=20,font=("bold",15))
label_3.place(x=10,y=280)
re=Entry(win,show="*",width=20)
re.place(x=240,y=280)
btn=Button(win,text="Submit",command=reset_pass,width=15,bg="black",fg="white").place(x=100,y=350)
btn=Button(win,text="Clear",command=reset_pass,width=15,bg="black",fg="white").place(x=250,y=350)
win.mainloop()