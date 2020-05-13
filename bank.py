from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import datetime
import time;
import sqlite3


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
    def query(self):
       
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        c.execute("SELECT *, oid FROM registerdb")
        records = c.fetchall()
        print(records)
         
        conn.commit()
        
        conn.close()



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
        
        self.LoginFrame2 = Frame(self.frame,width=1010,height=200,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
        self.btnbdetails = Label(self.LoginFrame1,text="Saurav Joshi(1811019)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=0,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Idrees Barnagarwala(1811004)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=1,column=0)
        self.btnbdetails = Label(self.LoginFrame1,text="Ronak Gala(1811011)",width=40,font=('arial',20,'bold'))
        self.btnbdetails.grid(row=2,column=0)
        
        self.btnquery = Button(self.LoginFrame2,text="Query Details",width=20,font=('arial',20,'bold'),command=self.query)
        self.btnquery.grid(row=0,column=0)
        

#Registration Window   
class Window2:
    def submit(self):
        
        conn = sqlite3.connect('registrationdb.db')
        
        #create a cursor
        c = conn.cursor()
        
        c.execute("INSERT INTO registerdb VALUES (:UserName,:Account_No,:Password,:address,:Money)",
            {
                'UserName': self.UserName.get(),
                'Account_No': self.Account_No.get(),
                'Password': self.Password.get(),
                'address': self.address.get(),
                'Money': self.Money.get(),
            })
         
        conn.commit()
        
        conn.close()
            
        
        
    def __init__(self,master):
        self.master = master
        self.master.title("Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        
        #create a table
        '''c.execute("""CREATE TABLE registerdb(
            UserName text,
            Account_No text,
            Password text,
            address text,
            Money text
            )""")'''
        
        self.Account_No=StringVar()
        self.Money=StringVar()
        self.UserName=StringVar()
        self.address=StringVar()
        self.Password=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Registration System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
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
        
        self.btnsubmit = Button(self.LoginFrame2,text="Submit Details",width=20,font=('arial',20,'bold'),command=self.submit)
        self.btnsubmit.grid(row=0,column=0)
        
        
        
        conn.commit()
        
        conn.close()
        

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
    
    
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        user = (self.Account_No.get())
        pas = (self.Password.get())
        
        c.execute("SELECT *, oid FROM registerdb")
        records = c.fetchall()
        #print(records)
        
        ok = 0 
        for record in records:
            if(user==str(record[1]) and pas==str(record[2])):
                ok=1
                break
        
        
        
        if(ok==1):
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
            #self.txtUsername.focus()
             
        conn.commit()
        
        conn.close()
         
    
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

        self.Account_No = StringVar()
        self.Money = StringVar()
        self.Password=StringVar()
        self.Password1=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Deposit System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
        self.lblAccount_No = Label(self.LoginFrame1,text="Enter the Account No.",font=('arial',30,'bold'),bd=22)
        self.lblAccount_No.grid(row=0,column=0)
        self.txtAccount_No = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Account_No)
        self.txtAccount_No.grid(row=0,column=1)
        
        self.lblMoney = Label(self.LoginFrame1,text="Enter the amount to be Deposited",font=('arial',30,'bold'),bd=22)
        self.lblMoney.grid(row=1,column=0)
        self.txtMoney = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Money)
        self.txtMoney.grid(row=1,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=2,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=2,column=1)
        
        self.lblPassword1 = Label(self.LoginFrame1,text="Re-Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword1.grid(row=3,column=0)
        self.txtPassword1 = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password1)
        self.txtPassword1.grid(row=3,column=1)
        
        self.btndep = Button(self.LoginFrame2,text="Submit Details",width=20,font=('arial',20,'bold'),command=self.submit_dep)
        self.btndep.grid(row=0,column=0)
        
    def submit_dep(self):
 
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        acc = (self.Account_No.get())
        money = (self.Money.get())
        pas = (self.Password.get())
        pas1 = (self.Password1.get())
        
        acc=str(acc)
        print(type(acc))
        
        #print(acc," ",money," ",pas)
        
        c.execute("SELECT *, oid FROM registerdb")
        records = c.fetchall()
        #print(records)
        
        ok = 0 
        for record in records:
            if(acc==str(record[1]) and pas==str(record[2]) and pas1==str(record[2])):
                value = record[4]
                break
        
        #print(records)
        
        now = int(value)
        add = int(money)
        so_far = now + add 
        so_far = str(so_far)

        #print(now," ",add," ",so_far)
        
        c.execute(" Update registerdb set Money = (?) WHERE Account_No = (?) and Password = (?) " ,(so_far,acc,pas))
        
       
        conn.commit()
        
        conn.close()
        




#Withdraw Window        
class Withdraw:
    def __init__(self,master):
        self.master = master
        self.master.title("Withdraw System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()    
        
        self.Account_No = StringVar()
        self.Money = StringVar()
        self.Password=StringVar()
        self.Password1=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Withdraw System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
        self.lblAccount_No = Label(self.LoginFrame1,text="Enter the Account No",font=('arial',30,'bold'),bd=22)
        self.lblAccount_No.grid(row=0,column=0)
        self.txtAccount_No = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Account_No)
        self.txtAccount_No.grid(row=0,column=1)
        
        self.lblMoney = Label(self.LoginFrame1,text="Enter the amount to be Withdrawn",font=('arial',30,'bold'),bd=22)
        self.lblMoney.grid(row=1,column=0)
        self.txtMoney = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Money)
        self.txtMoney.grid(row=1,column=1)
        
        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=2,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=2,column=1)
        
        self.lblPassword1 = Label(self.LoginFrame1,text="Re-Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword1.grid(row=3,column=0)
        self.txtPassword1 = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password1)
        self.txtPassword1.grid(row=3,column=1)
        
        self.btnwith = Button(self.LoginFrame2,text="Submit Details",width=20,font=('arial',20,'bold'),command=self.submit_with)
        self.btnwith.grid(row=0,column=0)
        
        
    def submit_with(self):
 
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        acc = (self.Account_No.get())
        money = (self.Money.get())
        pas = (self.Password.get())
        pas1 = (self.Password1.get())
        
        #print(acc," ",money," ",pas)
        
        c.execute("SELECT *, oid FROM registerdb")
        records = c.fetchall()
        #print(records)
        
        ok = 0 
        value = 0
        for record in records:
            if(acc==str(record[1]) and pas==str(record[2]) and pas1==str(record[2])):
                value = record[4]
                break
        
        #print(value)
        
        now = int(value)
        add = int(money)
        so_far = now - add 
        so_far1 = str(so_far)
        #print(now," ",add," ",so_far)
        
        if(so_far<0):
            tkinter.messagebox.askyesno("Bank Management System","Not enough balance to withdraw. Check your balance!!")
        else:
            c.execute(" Update registerdb set Money = (?) WHERE Account_No = (?) and Password = (?) " ,(so_far1,acc,pas))
            
        conn.commit()
        
        conn.close()
        


    
        
        
        

#Check Balance Window
class Check_Bal:
    def __init__(self,master):
        self.master = master
        self.master.title("Check Balance System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack() 

        self.Account_No = StringVar()
        self.Password=StringVar()
        self.Password1=StringVar()
        
        self.LabelTitle = Label(self.frame,text="Check Balance System",font=('arial',30,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.LoginFrame1 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=2010,height=300,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)
        
        self.LoginFrame3 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.LoginFrame3.grid(row=3,column=0)
        
        self.lblAccount_No = Label(self.LoginFrame1,text="Enter the Account No",font=('arial',30,'bold'),bd=22)
        self.lblAccount_No.grid(row=0,column=0)
        self.txtAccount_No = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Account_No)
        self.txtAccount_No.grid(row=0,column=1)

        self.lblPassword = Label(self.LoginFrame1,text="Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)
        
        self.lblPassword1 = Label(self.LoginFrame1,text="Re-Enter Password : ",font=('arial',30,'bold'),bd=22)
        self.lblPassword1.grid(row=2,column=0)
        self.txtPassword1 = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password1)
        self.txtPassword1.grid(row=2,column=1)
        
        self.btnmon = Button(self.LoginFrame2,text="Submit Details",width=20,font=('arial',20,'bold'),command=self.submit_check)
        self.btnmon.grid(row=0,column=0)
        
        
    def submit_check(self):
 
        conn = sqlite3.connect('registrationdb.db')
        
        c = conn.cursor()
        
        acc = (self.Account_No.get())
        pas = (self.Password.get())
        pas1 = (self.Password1.get())
        
        c.execute("SELECT *, oid FROM registerdb")
        records = c.fetchall()
        
        ok = 0 
        value = 0
        for record in records:
            if(acc==str(record[1]) and pas==str(record[2]) and pas1==str(record[2])):
                value = record[4]
                break
        
        self.lbldisplay = Label(self.LoginFrame3,text="Your balance is ",font=('arial',30,'bold'),bd=22)
        self.lbldisplay.grid(row=0,column=0)
        
        self.lbldisplaymoney = Label(self.LoginFrame3,text=value,font=('arial',30,'bold'),bd=22)
        self.lbldisplaymoney.grid(row=0,column=1)
       
        conn.commit()
        
        conn.close()
        
        
        

if __name__ == '__main__':
    main()


     