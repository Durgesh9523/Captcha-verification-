from tkinter import *
from PIL import ImageTk,Image
import string
import random
from tkinter.font import Font
from tkinter import messagebox
from captcha.image import ImageCaptcha
import sqlite3
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS data(
                    name text, 
                    email text, 
                    reg_no text, 
                    gender text, 
                    password text
                )
            ''')
con.commit()
root=Tk()
root.title("PASSWORD MANAGER")
root.config(background="#a7d9c5")
root.geometry('600x500')    
passowrd=StringVar()
regNo=StringVar()
capClear=StringVar()
letters=string.ascii_lowercase+string.digits+string.ascii_uppercase
ran = ''.join(random.choice(letters) for i in range(7))
image=ImageCaptcha(width=280,height=50)
data=image.generate(ran)
image.write(ran,'CAPTCHA.png')
img=ImageTk.PhotoImage(Image.open("CAPTCHA.png"))
img_label=Label(root,image=img)
photo_img=PhotoImage(file="icons-refresh-64.png")
photo=photo_img.subsample(3,3)
def Passowrd_changer():
    win=Tk()
    def reset_pass():
        old_pas=str(old.get())
        new_pas=str(new.get())
        re_pas=str(re.get())
        check_counter=0
        warn=""
        if old_pas=="":
            warn="Old passowrd cannot be Empty"
        else:
            check_counter+=1
        if new_pas=="":
            warn="New passowrd cannot be Empty"
        else:
            check_counter+=1
        if re_pas=="":
            warn="Confirm passowrd cannot be Empty"
        else:
            check_counter+=1
        if check_counter==3:
            if(old_pas==ol and new_pas==re_pas):
                try:
                    con = sqlite3.connect('userdata.db')
                    c = con.cursor()
                    c.execute("update data set password_p=:new_p where password_p=:old_p",{'new_p':new_pas,'old_p':old_pas})
                    con.commit()
                    messagebox.showinfo("Success","Password updated Successfully")
                    win.destroy()
                    clear() 
                except Exception as ep:
                        messagebox.showerror('', ep)
            elif(new_pas!=re_pas):
                messagebox.showerror('error','new passowrd does not match with confirm passowrd')
            else:
                messagebox.showerror('error','old passowrd does not match')
    win.geometry("500x500")
    re=regEnt1.get()
    ol=str(pssentry.get())
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
    win.mainloop()
def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        registration_no=[]
        pwd=[]
        for row in c.execute("Select * from data"):
            registration_no.append(str(row[2]))
            pwd.append(str(row[4]))
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname =str(regEnt1.get())
    upwd = str(pssentry.get())
    cap=str(capClear.get())
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if cap=="":
        warn="Captcha can't be empty"
    else:
        check_counter+=1
    if check_counter == 3:
        if (uname in registration_no and upwd in pwd and cap==ran):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            Passowrd_changer()
        elif(cap!=ran):
            messagebox.showerror('Login Status', 'invalid captcha')
            capClear.set("")
            refresh()
        else:
            messagebox.showerror('Login Status', 'invalid registration no or password')
            clear()
    else:
        messagebox.showerror('', warn)
def sign_in():
    window=Toplevel(root);
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
                window.destroy();

            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Error', warn)
    window.geometry("500x500")
    window.title('Registration form')
    label_0 =Label(window,text="Registration form", width=20,font=("bold",20))
    label_0.place(x=90,y=60)
    label_1 =Label(window,text="FullName", width=20,font=("bold",10))
    label_1.place(x=90,y=130)
    Name=Entry(window)
    Name.place(x=240,y=130)
    label_4 =Label(window,text="Registration_no", width=20,font=("bold",10))
    label_4.place(x=90,y=180)
    label_3 =Label(window,text="Email", width=20,font=("bold",10))
    label_3.place(x=90,y=280)
    email=Entry(window)
    email.place(x=240,y=280)
    Reg_no=Entry(window)
    Reg_no.place(x=240,y=180)
    Gender=Label(window,text="Gender", width=20,font=("bold",10))
    Gender.place(x=90,y=230)
    var=IntVar()
    Radiobutton(window,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
    Radiobutton(window,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)
    Password=Label(window,text="Create Password", width=20,font=("bold",10))
    Password.place(x=70,y=320)
    register_pwd = Entry(window,show='*')
    register_pwd.place(x=240,y=320)
    Button(window, text='Submit' ,command=insert_record, width=20,bg="black",fg='white').place(x=180,y=380)
    window.mainloop()
    
def cap_generator():
    global ran
    letters=string.ascii_lowercase+string.digits+string.ascii_uppercase
    ran = ''.join(random.choice(letters) for i in range(7))
    print(ran)
    image=ImageCaptcha(width=280,height=50)
    data=image.generate(ran)
    image.write(ran,'CAPTCHA.png')
def refresh():
    cap_generator() 
    img2=ImageTk.PhotoImage(Image.open("CAPTCHA.png"))
    img_label.configure(image=img2)
    img_label.image=img2
def clear():
    refresh()
    regNo.set("")
    passowrd.set("")
    capClear.set("")
nreg=Label(root,text="Reg No.",bg='#a7d9c5',font=Font(family="Rockwell",size=12)).place(x=170,y=100)
npwd=Label(root,text="Password",bg="#a7d9c5",font=Font(family="Rockwell",size=12)).place(x=170,y=150)
txx=Label(root,text="Type the code you see above *",font="none 10 bold italic",bg='#a7d9c5',fg="#e03267").place(x=280,y=280)
cappy=Label(root,text="Captcha",bg="#a7d9c5",font=Font(family="Rockwell",size=12)).place(x=170,y=220)
mssg=Label(root,text="Login To Your Account",bg="#a7d9c5",font=Font(family="Bodoni MT",size=25)).place(x=150,y=10)
regEnt1=Entry(root,textvariable=regNo,font=Font(family='Arial',size=10))
regEnt1.place(x=280,y=100,width=200,height=25)
pssentry=Entry(root,width=25,textvariable=passowrd,show='*',font=Font(family='Arial',size=10))
pssentry.place(x=280,y=150,width=200,height=25)
captchEntry=Entry(root,textvariable=capClear,font=Font(family='Arial',size=10)).place(x=280,y=320,width=200,height=25)
img_label.place(x=280,y=220)
signBtn=Button(root,text="Sign Up",command=sign_in,bg="#b6aed9",width=7,height=1,font=Font(family="Rockwell",size=12),border=3).place(x=480,y=380)
submitBtn=Button(root,text="Sign In",command=login_response,bg="#b6aed9",width=7,height=1,font=Font(family="Rockwell",size=12),border=3).place(x=280,y=380)
refereshBtn=Button(root,image=photo,border=2,height=20,width=20,command=refresh,bg="#e0e5ef").place(x=550,y=280)
#playbuttone=Button(root,text="Play",font=Font(family="Rockweel",size=12),width=7,height=1,bg="#b6aed9",command=play).place(x=750,y=280)
clrbutton=Button(root,text="clear",command=clear,width=7,height=1,font=Font(family="Rockwell",size=12),border=4,bg="#b6aed9").place(x=380,y=378)
root.mainloop()