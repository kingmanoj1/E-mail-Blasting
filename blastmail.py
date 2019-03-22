from tkinter import *
import smtplib
from email.mime.text import MIMEText
from tkinter.messagebox import showinfo
import re


r=Tk()

def blast():
    uname=e4.get()
    pas=e5.get()

    
    if re.match(r'[a-zA-Z0-9_]+@[a-z]+\.[a-zA-Z]{2,4}',uname) :
        frm=uname
        to=e1.get()
        mssg=t1.get("1.0",END)
        sub=e2.get()
        global n
        n=e3.get()
        m=str(n)   
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(uname,pas)

        if re.match(r'[a-zA-Z0-9_]+@[a-z]+\.[a-zA-Z]{2,4}',to):
            if m=='':
                showinfo("message","please enter no of mail")

            else:
                i=1
                while i<=n:
                    msg=MIMEText(mssg)
                    msg['Subject']=(sub+":"+str(i))
                    msg['From']=uname
                    msg['To']=to
                    s.send_message(msg)
                    i=i+1
                showinfo("message","message send")
        else:
            showinfo("message","Please check email address")
    else:
        showinfo("message","plz check Username or Password")



r.title("Email Blaster")
r.resizable(0,0)
r.wm_iconbitmap("eb.ico")
r.geometry('1000x680+140+0')

l1=Label(r,text="e-mail Blasting",font=('vardana',33),bg='blue',fg='white',activebackground='green')

l2=Label(r,text='To* :',font=('arial',15))
l3=Label(r,text="Subject*",font=('arial',15))
l4=Label(r,text='E-mail*',font=('arial',15))
l5=Label(r,text="How Many",font=('arial',15))
l6=Label(r,text="Username*",font=('arial',15))
l7=Label(r,text="Password*",font=('arial',15))


b1=Button(r,text="Send",font=('arial',15),command=blast)

e1=Entry(r,font=('arial',15))
e2=Entry(r,font=('arial',15))
e3=Entry(r,font=('arial',15))
e4=Entry(r,font=('arial',15))
e5=Entry(r,font=('arial',15))

t1=Text(r,width=60,height=18,font=('arial',14))

b1.place(x=450,y=580)

l1.place(x=340,y=5)
l2.place(x=161,y=110)
l3.place(x=122,y=140)
l4.place(x=131,y=170)
l5.place(x=100,y=588)
l6.place(x=100,y=75)
l7.place(x=500,y=75)

e1.place(x=200,y=110)
e2.place(x=200,y=140)
e3.place(x=200,y=588)
t1.place(x=200,y=170)
e4.place(x=200,y=75)
e5.place(x=620,y=75)

r.mainloop()