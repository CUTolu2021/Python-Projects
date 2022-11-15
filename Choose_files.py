from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Choose Your Files")
root.geometry("400x400")
#Set window background color
root.config(background = "white")

label_file_explorer = Label(root,
                            text = "File Explorer using Tkinter",
                            width = 50, height = 4,
                            fg = "blue")
label_file_explorer.grid(row=0,column=1)
#drop down code
options = ["Desktop","Documents","Downloads","Music","Videos","Pictures","PycharmProjects"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked,*options)
drop.grid(row=1,column=1,pady=10,padx=1)

#function for drop down menu
def show():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/omoniyi tolulope/"+clicked.get(),
                                               title="Select a file", filetypes=(("pdf files","*.pdf"),("MP3 File","*.mp3"),("jpg files","*.jpg"),("png files","*.png"),("All files", "*.*")))

Files = Button(root,text="Choose files",command=show,width=10)
Files.grid(row=2,column=1,padx=20,pady=2)
button_exit = Button(root,
                     text = "Exit",
                     command = exit,width=5)
button_exit.grid(row=3,column=1)
root.mainloop()