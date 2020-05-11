from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import datetime
import time;


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
    
#Main Screen    
class MainWindow:
    def __init__(self,master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.LabelTitle = Label(self.frame,text="Bank Management System",font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        
        self.btnLogin = Button(self.LoginFrame1,text="Login",width=20,font=('arial',20,'bold'),command=self.Login_window)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnRegister = Button(self.LoginFrame1,text="Register",width=20,font=('arial',20,'bold'),command=self.Registration_window)
        self.btnRegister.grid(row=0,column=1)
        
        self.btnschemes = Button(self.LoginFrame1,text="Schemes",width=20,font=('arial',20,'bold'),command=self.Schemes)
        self.btnschemes.grid(row=1,column=0)
        
        self.btnbdetails = Button(self.LoginFrame1,text="Bank Details",width=20,font=('arial',20,'bold'),command=self.Bank_Details)
        self.btnbdetails.grid(row=1,column=1)
        
        
    def  Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
    
    def Login_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window1(self.newWindow)
        
    def Schemes(self):
        self.newWindow = Toplevel(self.master)
        self.app = SchemesClass(self.newWindow)
        
    def Bank_Details(self):
        self.newWindow = Toplevel(self.master)
        self.app = BankDetailsClass(self.newWindow)
        
#scheme Details     
class SchemesClass:
    def __init__(self,master):
        self.master = master
        self.master.title("Rules")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.LabelTitle = Label(self.frame,text="Schemes System",font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.btnbdetails = Label(self.LoginFrame1,text="Deposit",width=20,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=0,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Withdrawal",width=20,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=1,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Checking Bank Balance",width=20,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=2,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Extra Schemes",width=20,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=3,column=0)
        
#Project Owner Details        
class BankDetailsClass:
    def __init__(self,master):
        self.master = master
        self.master.title("Bank Details")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.LabelTitle = Label(self.frame,text="Bank Management System Made By :-",font=('arial',40,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=1010,height=200,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.btnbdetails = Label(self.LoginFrame1,text="Saurav Joshi(1811019)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=0,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Idrees Barnagarwala(1811004)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=1,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Ronak Gala(1811012)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=2,column=0)


#Registration Window   
class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Account_No=StringVar()
        self.Money=int()
        self.UserName=StringVar()
        self.address=StringVar()
        self.Password=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Registration System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.lblUserName = Label(self.LoginFrame1,text="Enter UserName",font=('arial',30,'bold'),bd=22)
        self.lblUserName.grid(row=0,column=0)
        self.txtUserName = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.UserName)
        self.txtUserName.grid(row=0,column=1)
        
        self.lblAccount_No = Label(self.LoginFrame1,text="Enter Account No. : ",font=('arial',30,'bold'),bd=22)
        self.lblAccount_No.grid(row=1,column=0)
        self.txtAccount_No = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Account_No)
        self.txtAccount_No.grid(row=1,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=2,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=2,column=1)
        
        self.lbladdress = Label(self.LoginFrame1,text="Enter Address : ",font=('arial',30,'bold'),bd=22)
        self.lbladdress.grid(row=3,column=0)
        self.txtaddress = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.address)
        self.txtaddress.grid(row=3,column=1)
        
        self.lblMoney = Label(self.LoginFrame1,text="Enter Initial Amount : ",font=('arial',30,'bold'),bd=22)
        self.lblMoney.grid(row=4,column=0)
        self.txtMoney = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Money)
        self.txtMoney.grid(row=4,column=1)
        

#Login Window    
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Account_No=StringVar()
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
        self.lblAccount_No = Label(self.LoginFrame1,text="Account No.",font=('arial',30,'bold'),bd=22)
        self.lblAccount_No.grid(row=0,column=0)
        self.txtAccount_No = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Account_No)
        self.txtAccount_No.grid(row=0,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Password",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1,padx=85)
        #======================================================================
        
        self.btnLogin = Button(self.LoginFrame2,text="Login",width=20,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset = Button(self.LoginFrame2,text="Reset",width=20,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)
        
        self.btnExit = Button(self.LoginFrame2,text="Exit",width=20,font=('arial',20,'bold'),command=self.exit1)
        self.btnExit.grid(row=0,column=2)
        
        
        self.btnDeposit = Button(self.LoginFrame3,text="Deposit",width=20,font=('arial',20,'bold'),state=DISABLED,command=self.Deposit_Window)
        self.btnDeposit.grid(row=0,column=0)
        
        self.btnWithdraw = Button(self.LoginFrame3,text="Withdraw",width=20,font=('arial',20,'bold'),state=DISABLED,command=self.Withdraw_Window)
        self.btnWithdraw.grid(row=0,column=1)
        
        self.btncheckbal = Button(self.LoginFrame3,text="Chack Balance",width=20,font=('arial',20,'bold'),state=DISABLED,command=self.Check_Bal_Window)
        self.btncheckbal.grid(row=0,column=2)
        
    #=======================================================================
    
    def Login_System(self):
        user = (self.Account_No.get())
        pas = (self.Password.get())
        
        if(user == str(1234) and (pas == str(1234))):
            self.btnDeposit.config(state=NORMAL)
            self.btnWithdraw.config(state=NORMAL)
            self.btncheckbal.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Bank Management System","Invalid Login Details!!")
            self.btnDeposit.config(state=DISABLED)
            self.btnWithdraw.config(state=DISABLED)
            self.btncheckbal.config(state=DISABLED)
            self.Account_No.set("")
            self.Password.set("")
            self.txtUsername.focus()
    
    def Reset(self):
        self.btnDeposit.config(state=DISABLED)
        self.btnWithdraw.config(state=DISABLED)
        self.btncheckbal.config(state=DISABLED)
        self.Account_No.set("")
        self.Password.set("")
        self.txtUsername.focus() 
    
    def exit1(self):
        tkinter.messagebox.askyesno("Bank Management System","Confirm You Want to Exit")
        if(self.exit1 > 0):
            self.master.destroy()
            return 
    #=======================================================================
        
    def  Deposit_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Deposit(self.newWindow)
        
    def Withdraw_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Withdraw(self.newWindow)
    
    def Check_Bal_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Check_Bal(self.newWindow)
        

        
#Deposit Window        
class Deposit:
    def __init__(self,master):
        self.master = master
        self.master.title("Deposit System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()   

        self.Money = int
        self.Password=StringVar
        
        self.LabelTitle = Label(self.frame,text="Deposit System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.lblMoney = Label(self.LoginFrame1,text="Enter the amount to be Deposited",font=('arial',30,'bold'),bd=22)
        self.lblMoney.grid(row=0,column=0)
        self.txtMoney = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Money)
        self.txtMoney.grid(row=0,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)
        
        self.lblPassword1 = Label(self.LoginFrame1,text="Re-Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword1.grid(row=2,column=0)
        self.txtPassword1 = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword1.grid(row=2,column=1)
        
        
        

#Withdraw Window        
class Withdraw:
    def __init__(self,master):
        self.master = master
        self.master.title("Withdraw System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()    
        
        self.Money = int
        self.Password=StringVar
        
        self.LabelTitle = Label(self.frame,text="Withdraw System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.lblMoney = Label(self.LoginFrame1,text="Enter the amount to be Withdrawn",font=('arial',30,'bold'),bd=22)
        self.lblMoney.grid(row=0,column=0)
        self.txtMoney = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Money)
        self.txtMoney.grid(row=0,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)
        
        self.lblPassword1 = Label(self.LoginFrame1,text="Re-Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword1.grid(row=2,column=0)
        self.txtPassword1 = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword1.grid(row=2,column=1)
        
        
        
        
        

#Check Balance Window
class Check_Bal:
    def __init__(self,master):
        self.master = master
        self.master.title("Check Balance System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()    

if __name__ == '__main__':
    main()


     