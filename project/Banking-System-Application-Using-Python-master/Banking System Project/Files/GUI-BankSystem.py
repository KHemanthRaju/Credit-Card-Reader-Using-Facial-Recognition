import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime
import tkinter.font as tkFont


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="lightgray")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=0,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	tk.Label(creditwn,relief="flat",height=5,bg="lightgray",text="").pack()
	l1=tk.Label(creditwn,relief="flat",bg="lightgray",text="Amount to be credited")
	l1.pack(side="top")
	tk.Label(creditwn,relief="flat",height=1,bg="lightgray",text="").pack()
	e1=tk.Entry(creditwn,relief="flat")
	e1.pack(side="top")
	tk.Label(creditwn,relief="flat",height=1,bg="lightgray",text="").pack()
	b=tk.Button(creditwn,text="Credit",relief="raised",bg="green",fg="white",padx=5,pady=2,command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))

def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="lightgray")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=0,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	tk.Label(debitwn,relief="flat",height=5,bg="lightgray",text="").pack()
	l1=tk.Label(debitwn,relief="flat",bg="lightgray",text="Amount to be debited")
	l1.pack(side="top")
	tk.Label(debitwn,relief="flat",height=1,bg="lightgray",text="").pack()
	e1=tk.Entry(debitwn,relief="flat")
	e1.pack(side="top")
	tk.Label(debitwn,relief="flat",height=1,bg="lightgray",text="").pack()
	b=tk.Button(debitwn,text="Debit",relief="raised",padx=5,pady=2,bg="red",fg="white",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="lightgray")
	fr1=tk.Frame(disp_wn,bg="green")
	l_title=tk.Message(disp_wn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=0,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	tk.Label(disp_wn,text="", height=2,bg="lightgray").pack()
	l1=tk.Message(disp_wn,text="Your Transaction History",padx=100,pady=10,width=1000,bg="lightgray",fg="black",relief="flat")
	l1.config(font=("Arial","20","underline bold"))
	l1.pack(side="top")
	tk.Label(disp_wn,height=6,bg="lightgray").pack()
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="flat",width=2000)
		l.pack(side="top")

	b=tk.Button(disp_wn,text="Quit",padx=5,pady=2,bg="black",fg="white",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Hello "+name)
	rootwn.configure(background="lightgray")
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=0,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	tk.Label(rootwn,text="", height=1,bg="lightgray").pack()
	label=tk.Label(text="Logged in as: "+name,relief="ridge",padx=15,pady=10,bg="white",fg="red",anchor="center",justify="center")
	label.pack(side="top")

	b2=tk.Button(text="Credit",width=30,pady=5,command=lambda: Cr_Amt(accnt,name))
	b3=tk.Button(text="Debit",width=30,pady=5,command=lambda: De_Amt(accnt,name))
	b4=tk.Button(text="Balance",width=30,pady=5,command=lambda: disp_bal(accnt))
	b5=tk.Button(text="Transaction",width=30,pady=5,command=lambda: disp_tr_hist(accnt))
	b6=tk.Button(text="Logout",width=30,pady=5,command=lambda: logout(rootwn))
	
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=400)
	
def logout(master):
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if((is_number(name))  or (is_number(pin)==0)):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("600x300")
	loginwn.title("Login")
	loginwn.configure(bg="lightgray")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=5,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	tk.Label(loginwn,text="",height=2,bg="lightgray").pack()
	detail=tk.Message(loginwn,text="User Login",relief="flat",width=2000,padx=700,pady=5,fg="black",bg="lightgray",justify="center",anchor="center")
	detail.config(font=("Arial","20","underline bold"))
	detail.pack(side="top")
	tk.Label(loginwn,text="", height=6,bg="lightgray").pack()
	l1=tk.Label(loginwn,text="Account Holder:",relief="flat",bg="lightgray")
	l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.pack(side="top")
	tk.Label(loginwn,text="",height=1,bg="lightgray").pack()
	l2=tk.Label(loginwn,text="Account Number:",relief="flat",bg="lightgray")
	l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.pack(side="top")
	tk.Label(loginwn,text="",height=1,bg="lightgray").pack()
	l3=tk.Label(loginwn,text="PIN:",relief="flat",bg="lightgray")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,show="*")
	e3.pack(side="top")
	tk.Label(loginwn,text="",height=1,bg="lightgray").pack()
	b=tk.Button(text="Submit",bg="lightyellow",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")

	b1=tk.Button(text="Cancel",relief="raised",bg="black",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	b.place(x=620,y=430)
	b1.place(x=700,y=430)
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	
def Create():
	crwn=tk.Tk()
	crwn.geometry("600x300")
	crwn.title("Create Account")
	crwn.configure(bg="lightgray")
	fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="TIMES BANK",relief="raised",width=2000,padx=600,pady=5,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	tk.Label(crwn,text="",height=2,bg="lightgray").pack()
	detail=tk.Message(crwn,text="Account Holder Details",relief="flat",width=2000,padx=700,pady=5,fg="black",bg="lightgray",justify="center",anchor="center")
	detail.config(font=("Arial","20","underline bold"))
	detail.pack(side="top")
	tk.Label(crwn,text="", height=6,bg="lightgray").pack()
	l1=tk.Label(crwn,text="Full Name:",bg="lightgray")
	l1.pack(side="top")
	e1=tk.Entry(crwn,relief="ridge")
	e1.pack(side="top")
	tk.Label(crwn,text="",height=1,bg="lightgray").pack()
	l2=tk.Label(crwn,text="Opening Amount:",relief="flat",bg="lightgray")
	l2.pack(side="top")
	e2=tk.Entry(crwn,relief="ridge")
	e2.pack(side="top")
	tk.Label(crwn,text="",height=1,bg="lightgray").pack()
	l3=tk.Label(crwn,text="PIN:",relief="flat",bg="lightgray")
	l3.pack(side="top")
	e3=tk.Entry(crwn,show="*",relief="ridge")
	e3.pack(side="top")
	tk.Label(crwn,text="",height=1,bg="lightgray").pack()
	b2=tk.Button(text="upload face Id",bg="black")
	b2.pack(side="top")
	b=tk.Button(text="Submit",padx=5,pady=2,bg="lightgreen",relief="raised",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b.place(x=10,y=43)
	b2.place(x=20,y=43)
	
	crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return

def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Times Bank System")
	rootwn.configure(background='aqua')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="background.gif")
	x = tk.Label (image = bg_image)
	x.place(y=-400)
	l_title=tk.Message(text="Welcome to TIMES BANK",relief="raised",width=2000,padx=600,pady=5,fg="yellow",bg="blue",justify="center",anchor="center")
	l_title.config(font=("Broadway","40","bold"))
	l_title.pack(side="top")
	detail=tk.Message(rootwn,text="Main Menu",relief="flat",width=2000,padx=700,pady=5,fg="red",bg="pink",justify="center",anchor="center")
	detail.config(font=("Arial","20","underline bold"))
	detail.pack(side="top")
	btn=tkFont.Font(size=12)
	b1=tk.Button(text="Create New Account",width=30,pady=5,font=btn,command=Create)
	b2=tk.Button(text="Login",width=30,pady=5,font=btn,command=lambda: log_in(rootwn))
	b6=tk.Button(text="Exit",width=7,pady=0,font=btn,bg="black",fg="white",command=rootwn.destroy)
	b1.place(x=800,y=300)
	b2.place(x=800,y=400)	
	b6.place(x=1250,y=80)
	rootwn.mainloop()

Main_Menu()
