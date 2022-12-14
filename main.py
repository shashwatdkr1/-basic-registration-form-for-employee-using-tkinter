from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Registration Form")
root.geometry("400x400")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
empIdLabel = ttk.Label(frame, text="Employee ID")
empIdLabel.grid(column=0, row=0, sticky=W)
empId = ttk.Entry(frame)
empId.grid(column=1, row=0, sticky=(W, E))
nameLabel = ttk.Label(frame, text="Employee Name")
nameLabel.grid(column=0, row=1, sticky=W)
name = ttk.Entry(frame)
name.grid(column=1, row=1, sticky=(W, E))
jobLabel = ttk.Label(frame, text="Job")
jobLabel.grid(column=0, row=2, sticky=W)
job = ttk.Entry(frame)
job.grid(column=1, row=2, sticky=(W, E))
job.insert(0,"Manager")
employeeTypeLabel = ttk.Label(frame, text="Employee Type")
employeeTypeLabel.grid(column = 0,row = 3, sticky=W)
employeeTypeRadioButton1 = ttk.Radiobutton(frame,text = 
"Regular",value=0)
employeeTypeRadioButton1.grid(column=1, row=3, sticky=(W, E))
employeeTypeRadioButton2 = ttk.Radiobutton(frame,text = 
"Temporary",value=1)
employeeTypeRadioButton2.grid(column=2, row=3, sticky=(W, E))
salaryLabel = ttk.Label(frame,text = "Salary")
salaryLabel.grid(column = 0, row = 4, sticky = W)
salarySpinbox = ttk.Spinbox(frame,from_=0,to=20000)
salarySpinbox.grid(column=1, row=4, sticky=(W, E))
salarySpinbox.set("1000")
insertButton = ttk.Button(frame, text="Insert")
insertButton.grid(column=0, row=5, sticky=(W, E))
updateButton = ttk.Button(frame, text="Update")
updateButton.grid(column=1, row=5, sticky=(W, E))
deleteButton = ttk.Button(frame, text="Delete")
deleteButton.grid(column=0, row=6, sticky=(W, E))
selectButton = ttk.Button(frame, text="Select")
selectButton.grid(column=1, row=6, sticky=(W, E))
root.mainloop()