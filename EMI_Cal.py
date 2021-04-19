from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Home Loan Eligibility Calculator")
root.resizable(False,False)


def yesNo():
    salary = int(E4.get())
    interest = float(E3.get())
    interest1 = (interest/12/100)
    amt1= int(E5.get())
    amt2 = (1 + interest1) ** amt1
    amt3 = amt2 - 1
    amt4 = amt2 / amt3
    new_emi = salary * 0.505

    Loan_Amt = int(E2.get()) * interest1 * amt4
    Loan_emi = (new_emi / interest1) * (1/amt4)
    
    if salary > 20000:
        print(f5.config(text="Yes",fg="green",font="Bold")) 
    if salary == 0:
        messagebox.showwarning("Error","No information entered !")
    if salary < 20000 :
        print(f5.config(text="No",fg="red"))
    if Loan_Amt > 0 :
        print(f6.config(text='{:.2f}'.format(Loan_Amt)))
    if Loan_emi > 0 :
            print(f7.config(text='{:.2f}'.format(Loan_emi)))

    
'''  
    c = (1 + float(b))**(int(E5.get()))
    d = c - 1
    e = c / d

    EMI = Loan_Amt 
 '''
    
    
def clear():
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    f5.config(text="")
    f6.config(text="")
    f7.config(text="")
    E2.insert(0,"0")
    E3.insert(0,"0")
    E4.insert(0,"0")
    E5.insert(0,"0")



L1 = Label(root,text="Please enter the following details.   ")
L1.grid(row=0,column=0,columnspan=2)
L2 = Label(root,text="Loan Amount :",fg="orange")
L2.grid(row=1,column=0)
L3 = Label(root,text="Annual Inerest Rate :",fg="orange")
L3.grid(row=2,column=0)
L4 = Label(root,text="Monthly Salary :",fg="orange")
L4.grid(row=3,column=0)
L5 = Label(root,text="Tenure(Month) :",fg="orange")
L5.grid(row=4,column=0)

E2 = Entry(root,relief=SUNKEN)
E2.grid(row=1,column=1)
E2.insert(0,"0")
E3 = Entry(root,relief=SUNKEN)
E3.grid(row=2,column=1)
E3.insert(0,"0")
E4 = Entry(root,relief=SUNKEN)
E4.grid(row=3,column=1)
E4.insert(0,"0")
E5 = Entry(root,relief=SUNKEN)
E5.grid(row=4,column=1)
E5.insert(0,"0")


f1= Label(root,text="The output as per the calculator is displayed below.")
f1.grid(row=5,column=0,columnspan=2)

f2 = Label(root,text="Are you eligible for loan ? ",fg="blue")
f2.grid(row=6,column=0)
f3 = Label(root,text="EMI :",fg="blue")
f3.grid(row=7,column=0)
f4 = Label(root,text="Loan Amount your eligible for :",fg="blue")
f4.grid(row=8,column=0)

f5 = Label(root,text="")
f5.grid(row=6,column=1)
f6 = Label(root,text="")
f6.grid(row=7,column=1)
f7 = Label(root,text="")
f7.grid(row=8,column=1)


b1 = Button(root,text = "Submit Information",width=20,bg="light green",command=yesNo)
b1.grid(row=9,column=0,pady=5,padx=5)
b2 = Button(root,text = "Reset Information",width=20,bg="light green",command=clear)
b2.grid(row=9,column=1,pady=5,padx=5)

root.mainloop()