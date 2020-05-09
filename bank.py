from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import datetime
import time;


def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

    
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username=StringVar()
        self.Password=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Bank Management System",font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
        self.LoginFrame3 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.LoginFrame3.grid(row=3,column=0)
        
        #====================================================================
        self.lblUsername = Label(self.LoginFrame1,text="Username",font=('arial',30,'bold'),bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Password",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1,padx=85)
        #======================================================================
        
        self.btnLogin = Button(self.LoginFrame2,text="Login",width=20,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset = Button(self.LoginFrame2,text="Reset",width=20,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)
        
        self.btnExit = Button(self.LoginFrame2,text="Exit",width=20,font=('arial',20,'bold'),command=self.exit)
        self.btnExit.grid(row=0,column=2)
        
        
        self.btnRegistration = Button(self.LoginFrame3,text="Registrations Form",width=20,font=('arial',20,'bold'),state=DISABLED,command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)
        
        self.btnLogin = Button(self.LoginFrame3,text="Login Form",width=20,font=('arial',20,'bold'),state=DISABLED,command=self.Login_window)
        self.btnLogin.grid(row=0,column=1)
        
    #=======================================================================
    
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        
        if(user == str(1234) and (pas == str(1234))):
            self.btnRegistration.config(state=NORMAL)
            self.btnLogin.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Bank Management System","Invalid Login Details!!")
            self.btnRegistration.config(state=DISABLED)
            self.btnLogin.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    
    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnLogin.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus() 
    
    def exit(self):
        tkinter.messagebox.askyesno("Bank Management System","Confirm You Want to Exit")
        if(self.exit > 0):
            self.master.destroy()
            return 
    #=======================================================================
        
    def  Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
        
    def Login_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)
        
class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        
        
class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()       


if __name__ == '__main__':
    main()


     