import os
import tkinter as tk
from PIL import ImageTk, Image

# main screen
master = tk.Tk()
master.title('Best bank in town')
master.geometry('650x650')
master.config(bg='#87CEEB')
master.resizable(False, False)

# second screen
ActionW = tk.Tk()
ActionW.geometry('550x550')
ActionW.title('Dashboard')
ActionW.config(bg='#87CEEB')
ActionW.resizable(False, False)

ActionW.withdraw()

# image
img = Image.open('assets/bankLogo.jpg')
img = img.resize((350, 350))
img = ImageTk.PhotoImage(img)

# login functions
global detail_balance
global detail_id
global detail_name
global detail_addr
global detail_pass


def login_enter(event=None):
    global detail_id
    global detail_name
    global detail_addr
    global detail_pass
    global detail_balance

    existing_acc = os.listdir()
    log_id = Temp_idno.get()
    log_pass = Temp_pass.get()

    # conditions

    if len(log_id) != 10:
        tk.Label(text='Invalid id number!', font=('Arial', 9), bg='#87CEEB', fg="red").place(x=260, y=500)
        return
    for id in existing_acc:
        if id == log_id:
            tk.Label(text='Password :', font=('Arial Bold', 12), bg='#87CEEB').place(x=230, y=452)
            file = open(id, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            passw = file_data[3]
            if log_pass == passw:
                file = open(id, 'r')
                file_data = file.read()
                user_cred = file_data.split('\n')
                print(user_cred)
                detail_id = user_cred[0]
                detail_name = user_cred[1]
                detail_addr = user_cred[2]
                detail_pass = user_cred[3]
                detail_balance = user_cred[4]
                master.withdraw()
                ActionW.deiconify()
                return

            else:

                tk.Label(text='Wrong password!', font=('Arial', 9), bg='#87CEEB', fg="red").place(x=260, y=500)


class Window1:
    def _init_(self):
        super().__init__()

    def viewDetails(self):
        ActionW_view = tk.Tk()
        ActionW_view.geometry('350x400')
        ActionW_view.title('Details')
        ActionW_view.config(bg='#87CEEB')
        ActionW.withdraw()

        # labels
        label_Balance = tk.Label(ActionW_view, text=f'Balance:         {detail_balance} ', font=('Arial Bold', 12),
                                 bg="white")
        label_id_no = tk.Label(ActionW_view, text=f'Your id number is : {detail_id}', font=('Arial Bold', 12),
                               bg="white")
        label_address = tk.Label(ActionW_view, text=f'Your address is :         {detail_addr}', font=('Arial Bold', 12),
                                 bg='white')
        label_id_no.place(y=80)
        label_address.place(y=140)
        label_Balance.place(y=200)

        def back():
            ActionW.deiconify()
            ActionW_view.destroy()
            ActionW.mainloop()

        btn_return = tk.Button(ActionW_view, width=18, text='Return to previous page', command=back).place(x=110, y=350)

        ActionW_view.mainloop()


def vd():
    ActionW_view = Window1()
    ActionW_view.viewDetails()


# withdraw function

def withd():
    global detail_balance
    ActionW.withdraw()
    withd_w = tk.Tk()
    withd_w.title('Withdraw')
    withd_w.config(bg='#87CEEB')
    withd_w.geometry('350x350')

    with_e = tk.Entry(withd_w)
    with_e.place(x=105, y=100)

    def with_F(event=None):

        global detail_balance
        global detail_id

        file = open(detail_id, 'r')
        file_data = file.read()
        det = file_data.split('\n')
        detail_id = det[0]
        detail_name = det[1]
        detail_addr = det[2]
        detail_pass = det[3]
        detail_balance = det[4]

        try:
            with_am = with_e.get()
            with_am = int(with_am)
            balance = int(detail_balance)
            if balance - with_am < 0:
                tk.Label(withd_w, text='Insufficient fund!! ', font=('Arial', 9), bg='#87CEEB',
                         fg="red").place(x=115,
                                         y=200)
                return
            else:
                balance = balance - with_am
                balance = str(balance)
                det.pop()
                det.append(balance)

            tk.Label(withd_w, text=f'New balance is: {balance}', font=('Arial', 11), bg='#87CEEB', fg="red").place(
                x=115,
                y=200)
            # updating the file
            cr_file = open(detail_id, "w")
            cr_file.write(detail_id + '\n')
            cr_file.write(detail_name + '\n')
            cr_file.write(detail_addr + '\n')
            cr_file.write(detail_pass + '\n')
            cr_file.write(balance)
            cr_file.close()

            return
        except:
            tk.Label(withd_w, text='Enter a valid withdraw amount!', font=('Arial', 9), bg='#87CEEB', fg="red").place(
                x=100,
                y=200)
            return

    with_B = tk.Button(withd_w, text="Withdraw", command=with_F).place(x=140, y=150)

    def back():
        ActionW.deiconify()
        withd_w.destroy()
        ActionW.mainloop()

    withd_w.bind('<Return>', with_F)
    btn_return = tk.Button(withd_w, width=18, text='Return to previous page', command=back)
    btn_return.place(x=195, y=300)
    return


def dep():

    # window
    global detail_balance
    ActionW.withdraw()
    dep_w = tk.Tk()
    dep_w.title('Deposit')
    dep_w.config(bg='#87CEEB')
    dep_w.geometry('350x350')
    dep_w.resizable(False, False)
    dip_e = tk.Entry(dep_w)
    dip_e.place(x=105, y=100)

    def depfun(event=None):
        global detail_balance
        global detail_id

        file = open(detail_id, 'r')
        file_data = file.read()
        det = file_data.split('\n')
        detail_id = det[0]
        detail_name = det[1]
        detail_addr = det[2]
        detail_pass = det[3]
        detail_balance = det[4]

        try:
            dip_am = dip_e.get()
            dip_am = int(dip_am)
            balance = int(detail_balance)
            balance = balance + dip_am
            balance = str(balance)
            det.pop()
            det.append(balance)
            tk.Label(dep_w, text=f'New balance is: {balance}', font=('Arial', 11), bg='#87CEEB', fg="green").place(
                x=115,
                y=200)

            # updating the file
            cr_file = open(detail_id, "w")
            cr_file.write(detail_id + '\n')
            cr_file.write(detail_name + '\n')
            cr_file.write(detail_addr + '\n')
            cr_file.write(detail_pass + '\n')
            cr_file.write(balance)
            cr_file.close()

            return
        except:
            tk.Label(dep_w, text='Enter a valid withdraw amount!', font=('Arial', 9), bg='#87CEEB', fg="red").place(
                x=100,
                y=200)
            return

    dep_w.bind('<Return>', depfun)
    dip_B = tk.Button(dep_w, text="Deposit", command=depfun).place(x=140, y=150)

    # return button

    def back():
        ActionW.deiconify()
        dep_w.destroy()
        ActionW.mainloop()

    btn_return = tk.Button(dep_w, width=18, text='Return to previous page', command=back)
    btn_return.place(x=195, y=300)
    return


def login():
    global Temp_idno
    global Temp_pass


Temp_idno = tk.StringVar()
Temp_pass = tk.StringVar()

# entry
logpass = tk.Entry(width=25, show='*', textvariable=Temp_pass)
logpass.place(x=240, y=480)
logid = tk.Entry(width=25, textvariable=Temp_idno)
logid.place(x=240, y=430)

# labels

lbi = tk.Label(text='Id number :', font=('Arial Bold', 12), bg='#87CEEB').place(x=230, y=397)
lbp = tk.Label(text='Password :', font=('Arial Bold', 12), bg='#87CEEB').place(x=230, y=452)
tk.Label(master, image=img).place(x=145, y=15)


# register finish

def finish_log():
    try:
        name = t_name.get()
        id_no = t_id.get()
        id_no = int(id_no)
        id_no = str(id_no)
        address = t_address.get()
        password = t_pass.get()
        existing_acc = os.listdir()

        if name == '' or id_no == '' or address == '' or password == '':
            tk.Label(reg_screen, text='All fields are required!!', font=('Ariel Bold', 10), fg='red',
                     bg='#87CEEB').grid(
                column=0, row=6, sticky=tk.W, pady=15, padx=15)
            return
        if len(id_no) != 10:
            tk.Label(reg_screen, text='  ID number incorrect!!', font=('Ariel Bold', 10), fg='red', bg='#87CEEB').grid(
                column=0, row=6, sticky=tk.W, pady=15, padx=15)
            return
        if id_no in existing_acc:
            tk.Label(reg_screen, text='Id already in use!!', font=('Ariel Bold', 10), fg='red',
                     bg='#87CEEB').grid(column=0, row=6, sticky=tk.W, pady=15, padx=15)
            return
        if name.isdigit() == True:
            tk.Label(reg_screen, text='No digits allowed', font=('Ariel Bold', 10), fg='red',
                     bg='#87CEEB').grid(column=0, row=6, sticky=tk.W, pady=15, padx=15)
            return
        if id_no not in existing_acc:
            cr_file = open(id_no, "w")
            cr_file.write(id_no + '\n')
            cr_file.write(name + '\n')
            cr_file.write(address + '\n')
            cr_file.write(password + '\n')
            cr_file.write('0')
            cr_file.close()
            tk.Label(reg_screen, text='Account created', font=('Ariel Bold', 14), fg='green',
                     bg='#87CEEB').grid(column=0, row=6, sticky=tk.W, pady=15, padx=15)
            return
    except:
        tk.Label(reg_screen, text=' Missing information!!', font=('Ariel Bold', 10), fg='red',
                 bg='#87CEEB').grid(column=0, row=6, sticky=tk.W, pady=15, padx=15)

        return


def reg_fun():
    global t_name
    global t_address
    global t_id
    global t_pass
    global reg_screen

    reg_screen = tk.Toplevel(master)
    reg_screen.title('Register')
    reg_screen.geometry('365x200')
    reg_screen.config(bg='#87CEEB')
    reg_screen.resizable(False, False)

    t_name = tk.StringVar()
    t_address = tk.StringVar()
    t_id = tk.StringVar()
    t_pass = tk.StringVar()

    # labels

    tk.Label(reg_screen, text='Enter details below to register:', font=('Arial Bold', 12), bg=('#87CEEB')).grid(row=0,
                                                                                                                sticky=tk.N,
                                                                                                                pady=10)
    tk.Label(reg_screen, text='Enter your name:', font=('Arial Bold', 10), bg=('#87CEEB'), ).grid(row=1, sticky=tk.W,
                                                                                                  pady=2, padx=10)
    tk.Label(reg_screen, text='Enter your address:', font=('Arial Bold', 10), bg=('#87CEEB')).grid(row=2, sticky=tk.W,
                                                                                                   pady=2, padx=10)
    tk.Label(reg_screen, text='Enter id number:', font=('Arial Bold', 10), bg=('#87CEEB')).grid(row=3, sticky=tk.W,
                                                                                                pady=2, padx=10)
    tk.Label(reg_screen, text='Enter your password:', font=('Arial Bold', 10), bg=('#87CEEB')).grid(row=4, sticky=tk.W,
                                                                                                    pady=2, padx=10)

    # Entry box
    tk.Entry(reg_screen, textvariable=t_name).grid(row=1, column=1)
    tk.Entry(reg_screen, textvariable=t_address).grid(row=2, column=1)
    tk.Entry(reg_screen, textvariable=t_id).grid(row=3, column=1)
    tk.Entry(reg_screen, textvariable=t_pass, show='*').grid(row=4, column=1)

    tk.Button(reg_screen, text='Finish', font=('Arial Bold', 10), command=finish_log, width=10).grid(row=6, column=1,
                                                                                                     sticky=tk.E, pady=12,
                                                                                                     padx=10)


# buttons
btn_log = tk.Button(master, text='Login', font=('Arial Bold', 10), width=22, height=2, command=login_enter).place(x=227,
                                                                                                                  y=525)
btn_reg = tk.Button(master, text='register', width=22, height=2, font=('Arial Bold', 10), command=reg_fun).place(x=227, y=575)

# buttons
btn_wd = tk.Button(ActionW, command=withd, text='Withdraw', width=45, height=2)
btn_wd.place(x=110, y=325)
btn_dp = tk.Button(ActionW, command=dep, text='Deposit', width=45, height=2)
btn_dp.place(x=110, y=280)

# view details button
btn_viewDetails = tk.Button(ActionW, text='View Details', width=45, height=2, command=vd)
btn_viewDetails.place(x=110, y=370)


def back():
    master.deiconify()
    ActionW.withdraw()
    ActionW.mainloop()


btn_return = tk.Button(ActionW, width=18, text='Sign out', command=back).place(x=200, y=450)

master.bind('<Return>',login_enter)

master.bind('<Return>',login_enter)
master.mainloop()
