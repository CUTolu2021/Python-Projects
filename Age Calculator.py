from tkinter import *

root = Tk()
root.title("Age Calculator")
root.geometry("480x400")

# Background color
root.config(bg="#F7DC6F")

# Main Label
Main = Label(root, text="LETS FIND OUT HOW OLD YOU ARE.", pady=10, padx=20, font=("Helvetica", 18), bg="#F7DC6F")
Main.grid(row=0, column=0, columnspan=4, sticky="W")

# Year of Birth Label
YOR = Label(root, text="Please enter your year of birth:", font=("Helvetica", 12), bg="#F7DC6F")
YOR.grid(row=1, column=0, sticky="W", pady=(30, 0))

# Year of Birth Entry
e = Entry(root, width=20, bg="white", fg="black", borderwidth=5)
e.grid(row=1, column=1, padx=10, pady=(30, 0))

# Current Year Label
COR = Label(root, text="Please enter the current year:", font=("Helvetica", 12), bg="#F7DC6F")
COR.grid(row=2, column=0, sticky="W", pady=(30, 0))

# Current Year Entry
r = Entry(root, width=20, bg="white", fg="black", borderwidth=5)
r.grid(row=2, column=1, padx=10, pady=(30, 0))

# Function to calculate age
def age():
    lab = Label(root, text="You will be " + str(int(r.get()) - int(e.get())) + " before the end of the year " + str(r.get()), font=("Helvetica", 12), bg="#F7DC6F")
    lab.grid(row=4, column=0, columnspan=2, pady=(30, 0))

# Submit Button
Result = Button(root, text="SUBMIT", padx=20, pady=7, command=age, bg="#58D68D", fg="white", activebackground="#48C9B0", activeforeground="white")
Result.grid(row=3, column=0, columnspan=3, pady=(30, 0))

root.mainloop()