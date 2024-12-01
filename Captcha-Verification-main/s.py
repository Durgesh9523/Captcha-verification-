from tkinter import *
from tkinter import messagebox
import sqlite3
#Creating object 'root' of Tk()
root = Tk()
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS data(
                    name_s text, 
                    email text, 
                    reg_no number, 
                    gender text, 
                    password_p text
                )
            ''')
con.commit()
def insert_record():
    check_counter=0
    warn = ""
    if Name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if Reg_no.get() == "":
       warn = "Registration No can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1


    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 5:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO data VALUES (:name_p, :email, :reg_no, :gender,:password_p)", {
                            'name_p': Name.get(),
                            'email': email.get(),
                            'reg_no': Reg_no.get(),
                            'gender': var.get(),
                            'password_p': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Registration form", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=90,y=130)

#this will accept the input string text from the user.
Name=Entry(root)
Name.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=90,y=280)

email=Entry(root)
email.place(x=240,y=280)
label_4 =Label(root,text="Registration_no", width=20,font=("bold",10))
label_4.place(x=90,y=180)

Reg_no=Entry(root)
Reg_no.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
Gender=Label(root,text="Gender", width=20,font=("bold",10))
Gender.place(x=90,y=230)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)

##this creates 'Label' widget for Language and uses place() method.
Password=Label(root,text="New Password", width=20,font=("bold",10))
Password.place(x=70,y=320)
register_pwd = Entry(root)
register_pwd.place(x=240,y=320)
#this creates button for submitting the details provides by the user
Button(root, text='Submit' ,command=insert_record, width=20,bg="black",fg='white').place(x=180,y=380)


#this will run the mainloop.
root.mainloop()