from tkinter import *
root=Tk()
root.title("To do list")
root.geometry("1000x400")
import sqlite3
from tkinter import messagebox
root.config(background = "skyblue")
label_file_explorer = Label(root,
                            text = "To do list using Tkinter",
                            width = 50, height = 4,
                            fg = "blue",font="lucida 15")
label_file_explorer.grid(row=0,column=1)

#create a database or connect to one
conn = sqlite3.connect('To_dolist.db')

#create cursor its work is to collect commands
c = conn.cursor()
#create Table
#c.execute("""CREATE TABLE Todo (
#name text
 #)""")


#creating text boxes for input for the database
Name = Entry(root,width=30,borderwidth=2,border=2)
Name.grid(row=1,column=1,pady=3)


#labels for the text boxes
Label(root,text="PLEASE ENTER THE ITEMS HERE:",font="TimesNewRoman 15").grid(row=1,column=0,pady=10)

#fuction for adding stuff to data base
def add():
    if Name.get() == "":
        # show the error message
        messagebox.showerror("Input Error")

        return 0
    else:
        conn = sqlite3.connect('To_dolist.db')

        # create cursor its work is to collect commands
        c = conn.cursor()
        #insert into table
        c.execute("INSERT INTO Todo VALUES (:Name)",
        {
            'Name': Name.get()+"\n"
        })
        conn.commit()
        # close connection
        conn.close()
        Name.delete(0,END)
mybutton=Button(root,text="ADD TO CURRENT LIST",command=add)
mybutton.grid(row=4,column=1,pady=5)




#create query function
def show():
    conn = sqlite3.connect('To_dolist.db')

    # create cursor its work is to collect commands
    c = conn.cursor()
    #query the database
    c.execute("SELECT *,oid FROM Todo")
    records = c.fetchall()
    print_f=''
    for i in records:
        print_f +=str(i[1])+"." + str(i[0])+"\n"

    querylabel = Label(root, text=print_f,font="lucida 13",width=10,height=10)
    querylabel.grid(row=9,column=1,columnspan=10,pady=1,padx=2,sticky = NW)
    conn.commit()
    # close connection
    conn.close()

#crete query button to show the content on my console
query=Button(root,text="VIEW",command=show,background="blue",font="lucida 13")
query.grid(row=5,column=1,pady=(10,0))

#create function to delete a record
def delete():
    conn = sqlite3.connect('To_dolist.db')
    c = conn.cursor()
    PLACEHOLDER = delete_box.get()
    c.execute("DELETE from Todo WHERE oid=" + PLACEHOLDER)
    #NOT TTHAT YOU CAN ALSO USE "DELETE from animals WHERE Name='lion'") issue is if lion is in 5 places it will delete all

    conn.commit()
    # close connection
    conn.close()
    delete_box.delete(0, END)

#creating the box and label for the delete id
delete_boxlabel = Label(root,text="ITEM NUMBER:",font="TimesNewRoman 15")
delete_boxlabel.grid(row=7,column=0,pady=20)
delete_box = Entry(root,width=30)
delete_box.grid(row=7,column=1,pady=20)
#create delete button
deletebtn=Button(root, text="Delete record",command=delete)
deletebtn.grid(row=8,column=1)
#create update button
conn.commit()
#close connection
conn.close()
vertical = Scale(root, from_=0,to=1000)
vertical.grid(row=0,column=3,rowspan=3)
my_lab = Label(root,text=vertical.get())
def slide():
    my_lab = Label(root, text=vertical.get())
    root.geometry(str(1000)+ "x" +str(vertical.get()))

mybut=Button(root,text="ADJUST",command=slide).grid(row=2,column=2)


root.mainloop()