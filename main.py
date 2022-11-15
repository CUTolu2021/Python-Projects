from tkinter import *
root=Tk()
root.title("Age Calculator")
root.geometry("400x400")
root.config(background = "pink")

Main=Label(root,text="LETS FIND OUT HOW OLD YOU ARE.",pady=10,padx=20)
Main.grid(row=0,column=0,columnspan=4)
#ENTRY FOR YEAR OF BIRTH
YOR=Label(root,text="Please enter your year of birth:")
YOR.grid(row=1,column=0)
e=Entry(root,width=20,bg="white",fg="black",borderwidth=5)
e.grid(row=1,column=1,padx=10,pady=10)
COR=Label(root,text="Please enter the current year:")
COR.grid(row=2,column=0)
r=Entry(root,width=20,bg="white",fg="black",borderwidth=5)
r.grid(row=2,column=1,padx=10,pady=10)

#function
def age():
    lab = Label(root, text="You will be " + str(int(r.get()) - int(e.get()))+" before the end of the year "+ str(r.get()))
    lab.grid(row=4,column=0,columnspan=2)



#Button for result
Result=Button(root,text="SUBMIT",padx=20,pady=7,command=age)
Result.grid(row=3,column=0,columnspan=3)


root.mainloop()