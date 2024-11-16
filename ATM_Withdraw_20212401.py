import tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

balance = 10000

root = Tk()

root.title("ATM Whithdraw System")
root.geometry("1000x700+250+50")
root.resizable(False,False)
root.configure(bg="#17161b")


##definition withdraw

def withdraw_cash(cash):

    global balance

    if balance >= cash:
        confirm = messagebox.askyesno("confirm", "Do you confirm the withdrawal process?")

        balance -= cash
        label_result.config(text=f"BALANCE: {balance} TL")
        messagebox.showinfo("info", f"BALANCE: {balance + cash} - {cash} \n\nNEW BALANCE: {balance} TL")
    else:
        messagebox.showinfo("info", "insufficient funds!")
        label_result.config(text="insufficient funds!")



##Definition Other withdraw button

def other_withdraw():
    global balance
    cash = simpledialog.askfloat("withdraw", "Enter the amount you wish to withdraw:", minvalue=1)

    if cash is not None:
        if balance >= cash:
            confirm = messagebox.askyesno("confirm", "Do you confirm the withdrawal process?")
            balance -= cash
            label_result.config(text=f"BALANCE: {balance} TL")
            messagebox.showinfo("info", f"BALANCE: {balance + cash} - {cash} \n\nNEW BALANCE: {balance} TL")
        else:
            messagebox.showinfo("info", "insufficient funds!")




##Definition exit button
def exit_atm():

    exit = messagebox.askyesno("EXIT", "DO YOU WANT TO EXIT?:")
    
    
    root.destroy()



##text label show balance
label_result= Label(root,width=20,height=2,text=f"BALANCE: {balance} TL",font=("arial",30,"bold"))
label_result.pack()


##text label bank name
label_text1 = Label(root, text='InfoSuperBANK',bg="#17161b", fg="#3697f5",font=("arial",30,"bold"))
label_text1.pack()
label_text1.place(x=360,y=250)

label_text2 = Label(root, text='ATM',bg="#17161b", fg="#3697f5",font=("arial",30,"bold"))
label_text2.pack()
label_text2.place(x=460,y=300)

label_text3 = Label(root, text='WELCOME TO',bg="#17161b", fg="#3697f5",font=("arial",10,"bold"))
label_text3.pack()
label_text3.place(x=360,y=238)


##text label Company name

label_text4 = Label(root, text='MADE by JANES TECHNOLOGY',bg="#17161b", fg="#3697f5",font=("italic",10,"bold"))
label_text4.pack()
label_text4.place(x=10,y=650)





##button

Button(root,text="20 TL", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=lambda: withdraw_cash(20)).place(x=10,y=200)
Button(root,text="50 TL", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=lambda: withdraw_cash(50)).place(x=10,y=300)
Button(root,text="100 TL", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=lambda: withdraw_cash(100)).place(x=10,y=400)
Button(root,text="150 TL", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=lambda: withdraw_cash(150)).place(x=790,y=200)
Button(root,text="200 TL", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=lambda: withdraw_cash(200)).place(x=790,y=300)


##other button
Button(root,text="OTHER ", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#3697f5",command=other_withdraw).place(x=790,y=400)


##EXIT BUTTON
Button(root,text="EXIT ", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#fff", bg="#FF4040",command=exit_atm).place(x=400,y=500)


root.mainloop()