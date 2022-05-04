from glob import glob
from shutil import unregister_unpack_format
import tkinter
import sqlite3, string
from tkinter import *
import time

# write a program to check if given string is number or not.
from colorama.ansi import clear_screen

conn = sqlite3.connect('C:/btu python/SHAGU.db')

c = conn.cursor()

def login_verify():
    global username1, usern, passw, wrongLabel
    global password1
    username1 = username_entry.get()
    password1 = password_entry.get()
    c.execute('''SELECT gmail, password FROM user where gmail = ? and password = ?''', (username1, password1))
    global labell
    if len(c.fetchall()) > 0:
        c.execute('''SELECT gmail, password FROM user where gmail = ? and password = ?''', (username1, password1))
        for row in c.fetchall():
            usern = row[0]
            passw = row[1]
        if username1 == usern and password1 == passw:
            profile_screen()
    elif username1 == "admin@gmail.com" and password1 == "admin":
        admin_screen()
    elif len(c.fetchall()) == 0 and for_wrong_username == None:
        labell = True
        wrongLabel = Label(text="Wrong username or password", fg="red", font=("calibri", 11))
        wrongLabel.pack()




def main_screen():
    global gmail, pasw, username_entry, password_entry, login_button, register_button, label
    global for_wrong_username, for_unfilled_fields
    for_wrong_username = None
    for_unfilled_fields = None
    global main_screenn
    main_screenn = Tk()
    # main_screenn.iconbitmap("C:/btu python/sturua/tkinter/hell.jpg")
    main_screenn.geometry("700x500")
    main_screenn.title("Login")
    label = Label(text="Please enter details below", fg='#000000')
    label.pack()
    gmail = Label(text="Gmail: ")
    gmail.pack()
    username_entry = Entry()
    password_entry = Entry(show='*')
    username_entry.pack()
    pasw = Label(text="Password: ")
    pasw.pack()
    password_entry.pack()
    login_button = Button(text="Login", command=login_verify)
    login_button.pack()

    register_button = Button(text="Register", command=register_user)
    register_button.pack()
    main_screenn.mainloop()
def register_user():
    global username, password, mail, age, surname
    gmail.pack_forget()
    pasw.pack_forget()
    username_entry.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    register_button.pack_forget()
    username = StringVar()
    surname = StringVar()
    mail = StringVar()
    age = StringVar()
    password = StringVar()
    global user_entry, user_label, surn_entry, surn_label, mail_entry, mail_label, age_entry, age_label, pass_entry, pass_label, reg_butt, unfilled
    user_label = Label(text="Username: ")
    user_label.pack()
    user_entry = Entry(textvariable=username)
    user_entry.pack()
    surn_label = Label(text="Surname: ")
    surn_label.pack()
    surn_entry = Entry(textvariable=surname)
    surn_entry.pack()
    mail_label = Label(text="Mail: ")
    mail_label.pack()
    mail_entry = Entry(textvariable=mail)
    mail_entry.pack()
    age_label = Label(text="age: ")
    age_label.pack()
    age_entry = Entry(textvariable=age)
    age_entry.pack()
    pass_label = Label(text="password: ")
    pass_label.pack()
    pass_entry = Entry(textvariable=password, show='*')
    pass_entry.pack()
    unfilled = Label(text="There are unfilled fields or incorrect mail,age", fg="red", font=("calibri", 11))
    reg_butt = Button(text="Registration", command=registration)
    reg_butt.pack()


def registration():
    mail_infoo = mail.get()
    global for_mail_info, for_unfilled_fields
    if "@" in mail_infoo and "." in mail_infoo:
        for_mail_info = True
    else:
        for_mail_info = False
        
    if len(username.get()) != 0 and len(password.get()) != 0 and len(mail.get()) != 0 and len(age.get()) != 0 and len(surname.get()) != 0 and for_mail_info and age.get().isdigit():
        global mail_info
        label.pack_forget()
        unfilled.pack_forget()
        user_entry.pack_forget()
        user_label.pack_forget()
        surn_entry.pack_forget()
        surn_label.pack_forget()
        mail_entry.pack_forget()
        mail_label.pack_forget()
        age_entry.pack_forget()
        age_label.pack_forget()
        pass_entry.pack_forget()
        pass_label.pack_forget()
        reg_butt.pack_forget()
        username_info = username.get()
        password_info = password.get()
        mail_info = mail.get()
        age_info = age.get()
        surname_info = surname.get()
        c.execute('''INSERT INTO user (NAME,SURNAME,GMAIL,AGE,PASSWORD,BALANCE) VALUES (?,?,?,?,?,?)''',(username_info, surname_info, mail_info, age_info, password_info,0))
        conn.commit()
        global reg_label, user, passs, maill, agee, surn
        reg_label = tkinter.Label(text="Registration Successful", fg='#000000').pack()
        Label(text="Your Information").pack()
        user = tkinter.Label(text="Username: " + username_info , fg='#000000').pack()
        surn = tkinter.Label(text="Surname: " + surname_info,fg='#000000').pack()
        maill = tkinter.Label(text="Mail: " + mail_info,fg='#000000').pack()
        agee = tkinter.Label(text="Age: " + age_info,fg='#000000').pack()
        passs = tkinter.Label(text="Password: " + password_info,fg='#000000').pack()
    else:
        if for_unfilled_fields == None:
            for_unfilled_fields = True
            unfilled.pack()
def admin_screen():
    global admin_screenn
    admin_screenn = tkinter.Tk()
    admin_screenn.geometry("700x600")
    admin_screenn.title("Admin")
    Label(admin_screenn,text="Welcome to the admin page", fg='#000000').pack()
    Label(admin_screenn, text="All Accounts", fg='#000000', font=("BPG Nino Mtavruli", 20)).pack()
    c.execute('''SELECT * FROM user''')
    conn.commit()
    for row in c.fetchall():
        Label(admin_screenn, text="Username: " + row[0] + " || Surname: " + row[1] + " || Mail: " + row[2] + " || Age: " + str(row[3]) + " || Password: " + row[4] + " || Balance: " + str(row[5])).pack()


    admin_screenn.mainloop()

def profile_screen():
    global info, transaction_button, wrongLabel
    wrongLabel.pack_forget()
    gmail.pack_forget()
    pasw.pack_forget()
    username_entry.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    register_button.pack_forget()
    label.pack_forget()
    Label(text="Welcome to your profile", fg='#000000').pack()
    c.execute('''SELECT * FROM user where GMAIL = ? and password = ?''',(username1, password1))
    conn.commit()
    for row in c.fetchall():
        info = Label(text="Username: " + row[0] + "\n Surname: " + row[1] + "\n Mail: " + row[2] + "\n Age: " + str(row[3]) + "\n Password: " + row[4] + "\n Balance: " + str(row[5]))
        info.pack()
      
main_screen()
conn.close()