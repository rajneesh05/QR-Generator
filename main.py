from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import os

def createFolder(directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

createFolder('./QR Code/')

class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x510+200+50")
        self.root.title("QR Generator | Developed by Rajneesh")
        self.root.resizable(False,False)
        self.root.config(bg="azure")

        title=Label(self.root, text="QR Code Generator", font=("time new roman",40),bg="black",fg="white",bd=7,relief=RIDGE).place(x=0,y=0,relwidth=1)

        #----------Employee Details window-----------
        #-------Variables--------
        self.var_empid=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        emp_f=Frame(self.root,bd=4,relief=RIDGE,bg='powderblue')
        emp_f.place(x=30,y=100,width=500,height=380)

        emp_title=Label(emp_f,text="Employee Details",font=('goudy old style',20),bg="gray",fg="white",bd=5,relief="raise").place(x=0,y=0, relwidth=1)
        lbl_id=Label(emp_f,text="Employee ID",font=('time new roman',15,'bold'),bg="powderblue").place(x=20,y=70)
        lbl_name=Label(emp_f,text="Name",font=('time new roman',15,'bold'),bg="powderblue").place(x=20,y=115)
        lbl_department=Label(emp_f,text="Department",font=('time new roman',15,'bold'),bg="powderblue").place(x=20,y=160)
        lbl_designation=Label(emp_f,text="Designation",font=('time new roman',15,'bold'),bg="powderblue").place(x=20,y=205)

        txt_id=Entry(emp_f,bd=3,justify=RIGHT,font=('time new roman',15),bg="lightyellow",textvariable=self.var_empid).place(x=200,y=70)
        txt_name=Entry(emp_f,bd=3,font=('time new roman',15),bg="lightyellow",textvariable=self.var_name).place(x=200,y=115)
        txt_department=Entry(emp_f,bd=3,font=('time new roman',15),bg="lightyellow",textvariable=self.var_department).place(x=200,y=160)
        txt_designation=Entry(emp_f,bd=3,font=('time new roman',15),bg="lightyellow",textvariable=self.var_designation).place(x=200,y=205)

        btn_generate=Button(emp_f,text='QR Generate',command=self.generate,font=('time new roman',15,'bold'),bg="green",fg="white",bd=4,relief=RAISED).place(x=165,y=260,width=150,height=38)
        btn_clear=Button(emp_f,text='Clear',command=self.clear,font=('time new roman',15,'bold'),bg="gray",fg="white",bd=4,relief=RAISED).place(x=348,y=260,width=77,height=38)

        self.msg=""
        self.lbl_msg=Label(emp_f,text=self.msg,font=('time new roman',20,'bold'),bg='powderblue',fg='green')
        self.lbl_msg.place(x=0,y=315,relwidth=1)

         #------Employee QR Code window-----------
        qr_f=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        qr_f.place(x=570,y=100,width=300,height=380)

        qr_title=Label(qr_f,text="Employee QR Code",font=('goudy old style',20),bg="gray",fg="white",bd=5,relief="raise").place(x=0,y=0, relwidth=1)    

        self.qr_code=Label(qr_f,text="QR Code\nNot Available",font=('times new roman',15),bg="black",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=40,y=90,width=215,height=230)

    def clear(self):
        self.var_empid.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")

    def generate(self):
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_department.get()=="" or self.var_designation.get()=="":
            self.msg="All Fields are Required!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID:{self.var_empid.get()}\n Employee Name:{self.var_name.get()}\n Department:{self.var_department.get()}\n Designation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[200,220])
            qr_code.save("QR Code/Emp_"+str(self.var_empid.get()+'.png'))
            #---------QR Code Image Update-----------
            self.img=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.img)
            #-----------Updating Notification--------------
            self.msg="QR Generated Successfully !!"
            self.lbl_msg.config(text=self.msg,fg='green')



root=Tk()
qr=Qr_Generator(root)
root.mainloop()