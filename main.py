from tkinter import *
from tkinter import ttk    # to use combo box
from tkinter import messagebox
from db import Mydatabase
db=Mydatabase('employee.db')

root = Tk()     #any name instead of root

#screen size
root.title('Employee management System')
root.geometry('1366x768+0+0')       #x=0,y=0
root.config(bg='lightblue')

name = StringVar()
age  = StringVar()
doj  = StringVar()
gender = StringVar()
email  = StringVar()
contact = StringVar()

#entry Frame
entries_frame = Frame(root,bg='orange')
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text='Employee Management system',font=('Calibri',18,'bold'),bg='orange',fg='white')
title.grid(row=0,columnspan=2,padx=10,pady=20)

#Entry Frame name box
lblName = Label(entries_frame,text='Name',font=('Calibri',16),bg='orange')
lblName.grid(row=1,column=0,padx=10,pady=10,sticky='w')
txtName = Entry(entries_frame,textvariable=name,font=('Calibri',16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky='w')

#Entry Frame age box
lblAge = Label(entries_frame,text='Age',font=('Calibri',16),bg='orange')
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtAge = Entry(entries_frame,textvariable=age,font=('Calibri',16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky='w')

#Entry Frame Doj box
lblDoj = Label(entries_frame,text='D.O.J',font=('Calibri',16),bg='orange')
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky='w')
txtDoj = Entry(entries_frame,textvariable=doj,font=('Calibri',16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')


#Entry Frame email box
lblEmail = Label(entries_frame,text='Email',font=('Calibri',16),bg='orange')
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky='w')
txtEmail = Entry(entries_frame,textvariable=email,font=('Calibri',16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky='w')

#Entry Frame Gender box
lblGender = Label(entries_frame,text='Gender',font=('Calibri',16),bg='orange')
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky='w')
comboGender = ttk.Combobox(entries_frame,font=('Calibri',16),width=28,textvariable=gender,state='readonly')
comboGender['values'] = ('MAle','Female')
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky='w')

#Entry Frame Contact box
lblContact = Label(entries_frame,text='Contact No',font=('Calibri',16),bg='orange')
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtContact = Entry(entries_frame,textvariable=contact,font=('Calibri',16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky='w')

#Entry Frame Address box
lblAddress = Label(entries_frame,text='Address',font=('Calibri',16),bg='orange')
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky='w')
txtAddress=Text(entries_frame,width=85,height=5,font=('Calibri',16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky='w')

def getData(event):
    selected_row =tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END,row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for resdata in db.Getalldata():
        tv.insert('',END,values=resdata)
def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()==" " or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()==" " or txtAddress.get(1.0,END)==" " :
        messagebox.showerror("Error in Input",'Please fill all the details')
        return
    db.Insert(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),   txtAddress.get(1.0,END))
    messagebox.showinfo('success','Record added Successfully')
    clearall()
    displayAll()


def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()==" " or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()==" " or txtAddress.get(1.0,END)==" " :
        messagebox.showerror("Error in Input",'Please fill all the details')
        return
    db.Update_record(row[0],txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),   txtAddress.get(1.0,END))
    messagebox.showinfo('success','Record Updated Successfully')
    clearall()
    displayAll()


def delete_employee():
    db.Delete_record(row[0])
    clearall()
    displayAll()

def clearall():
    name.set('')
    age.set('')
    doj.set('')
    gender.set('')
    email.set('')
    contact.set('')
    txtAddress.delete(1.0,END)



btn_frame=Frame(entries_frame,bg='orange')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')

btnAdd=Button(btn_frame,command=add_employee,text='Add details',width=15,font=('Calibri',16,'bold'),bd='0',bg='green').grid(row=0,column=0,padx=10)


btnUpdate=Button(btn_frame,command= update_employee,text='Update details',width=15,font=('Calibri',16,'bold'),bd='0',bg='lightgreen').grid(row=0,column=1,padx=10)


btnDelete=Button(btn_frame,command=delete_employee,text='Delete details',width=15,font=('Calibri',16,'bold'),bd='0',bg='red').grid(row=0,column=2,padx=10)


btnClear=Button(btn_frame,command=clearall,text='Clear details',width=15,font=('Calibri',16,'bold'),bd='0',bg='purple').grid(row=0,column=3,padx=10)




#Table frame
tree_frame = Frame(root,bg='lightgreen')
tree_frame.place(x=0,y=500,width=1366,height=400)

style = ttk.Style()
style.configure('mystyle.Treeview.heading',font=('calibri',18))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8))
tv.heading('1',text='ID')
tv.column('1',width=5)
tv.heading('2',text='Name')
tv.heading('3',text='Age')
tv.column('3',width=15)
tv.heading('4',text='D.O.J')
tv.heading('5',text='Email')
tv.heading('6',text='Gender')
tv.heading('7',text='Contact')
tv.heading('8',text='Address')
tv['show'] ='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()
displayAll()

root.mainloop()    #run continously









