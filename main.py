from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class ConnectionDatabase:
	def __init__(self):
		self._db = sqlite3.connect('informationDB.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists complainTable(ID integer primary key autoincrement, Name varchar(255), Mobile varchar(255), Address Text, Role varchar(255), Comment text)')
		self._db.commit()
	def Add(self,name,mobile,address,role,comment):
		self._db.execute('insert into complainTable (Name, Mobile, Address, Role, Comment) values (?,?,?,?,?)', (name, mobile, address, role, comment))
		self._db.commit()
		return 'Your complaint has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from complainTable')
		return cursor

class ComplaintListing:
    def __init__(self):
        self.connectionDB = ConnectionDatabase()
        self.connectionDB.row_factory = sqlite3.Row
        self.root = Tk()
        self.root.title('List of Complaints')
        tree = Treeview(self.root)
        tree.pack()
        tree.heading('#0', text='ID')
        tree.configure(column=('#Name', '#Mobile', '#Address', '#Role', '#Comment'))
        tree.heading('#Name', text='Name')
        tree.heading('#Mobile', text='Mobile No')
        tree.heading('#Address', text='Address')
        tree.heading('#Role', text='Role')
        tree.heading('#Comment', text='Comment')
        tree.column('#0', stretch=NO, minwidth=0, width=100)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=100)
        tree.column('#4', stretch=NO, minwidth=0, width=100)
        tree.column('#5', stretch=NO, minwidth=0, width=300)
        cursor = self.connectionDB.ListRequest()
        for row in cursor:
            tree.insert('', 'end', '#{}'.format(row['ID']), text=row['ID'])
            tree.set('#{}'.format(row['ID']), '#Name', row['Name'])
            tree.set('#{}'.format(row['ID']), '#Mobile', row['Mobile'])
            tree.set('#{}'.format(row['ID']), '#Address', row['Address'])
            tree.set('#{}'.format(row['ID']), '#Role', row['Role'])
            tree.set('#{}'.format(row['ID']), '#Comment', row['Comment'])

#Config

conn = ConnectionDatabase()
root = Tk()
root.geometry('550x350')
root.title('Complaint Management System')
root.configure(bg='#AEB6BF')

#Style
style = Style()
style.theme_use('classic')
for styles in ['TLabel', 'TButton', 'TRadioButton']:
    style.configure(styles, bg='#AEB6BF')


labels = ['Name:', 'Mobile No:', 'Address:', 'Role:', 'Comment:']
for i in range(5):
    Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

ButtonList = Button(root, text='View Complain')
ButtonList.grid(row=5, column=1)

ButtonSubmit = Button(root, text='Submit Now')
ButtonSubmit.grid(row=5, column=2)

# Entries
name = Entry(root, width=40, font=('Arial', 14))
name.grid(row=0, column=1, columnspan=2)

mobile = Entry(root, width=30, font=('Arial', 14))
mobile.grid(row=1, column=1, columnspan=1)

address = Entry(root, width=40, font=('Arial', 14))
address.grid(row=2, column=1, columnspan=2)

Group = StringVar()
Radiobutton(root, text='Employee', value='Employee', variable=Group).grid(row=3, column=1)
Radiobutton(root, text='User', value='User', variable=Group).grid(row=3, column=2)


comment = Text(root, width=40, height=5, font=('Arial', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
    message = conn.Add(name.get(), mobile.get(), address.get(), Group.get(), comment.get(1.0, 'end'))
    name.delete(0,'end')
    mobile.delete(0, 'end')
    address.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)

def ShowComplainList():

    listrequest = ComplaintListing()


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)

root.mainloop()
