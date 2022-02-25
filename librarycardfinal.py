from tkinter import *
from PIL import ImageTk, Image
import datetime
from tabulate import tabulate
from tkinter import messagebox
import mysql.connector
import tkcap
import os

mydb = mysql.connector.connect(host='localhost', user='root', passwd='Nidhikarkera0', database='library')
mycursor = mydb.cursor()

root = Tk() #creating the window
root.configure(bg='LightSkyBlue1')
root.geometry('800x400')
root.title('GreyStone Library')

def mem_details():
        global memID
        memID = int(input("Enter the member ID: "))
        mycursor.execute(f"select * from members where MemID={memID}")
        details = mycursor.fetchall()
        disp(details[0])
             
def disp(details):
        img_logo = Image.open("C:/Users/karke/OneDrive/Desktop/cs project file/final/library_card_logo.png")  # logo img path
        resized = img_logo.resize((73, 71), Image.ANTIALIAS)
        photo_logo = ImageTk.PhotoImage(resized)
        imglb_logo = Label(root, image=photo_logo, relief='raised', bg='LightSkyBlue1', borderwidth=5)
        imglb_logo.pack() #shoving it onto the window
        imglb_logo.place(x=25,y=10)

        title = Label(root, text='Grey Stone Library📖', bg='LightSkyBlue1', fg='maroon',
                          font=('Georgia', 40))
        title.pack()
        title.place(x=125,y=30)

        sep = '_________' * 50
        sep_label = Label(root, text=sep, bg='navy', fg='navy',
                              font=('Script MT Bold', 15, 'bold'))
        sep_label.pack()
        sep_label.place(y=100)

        date_today = datetime.date.today()
        year = date_today.year
        month = date_today.strftime("%B")
        subj = f' Library Card {month} {year}'.upper()
        libcard = Label(root, text=subj, bg='LightSkyBlue1', fg='brown4', font=('Century', 10, 'bold'))
        libcard.pack()
        libcard.place(x=200,y=135)

        memid = Label(root, text='Member Id                : ' + str(details[0]), bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        memid.place(x=10, y=190)

        name = Label(root, text='Member Name          : ' + details[1], bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        name.place(x=10, y=230)

        regdate = details[10]
        regmonth = regdate.strftime("%B")
        regdate = f'{regdate.day} {regmonth} {regdate.year}'

        dor = Label(root, text='Date of Registration  : ' + regdate, bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        dor.place(x=10, y=270)

        no = Label(root, text='Contact No     : ' + str(details[4]), bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        no.place(x=400, y=190)

        dob = details[2]
        dobmonth = dob.strftime("%B")
        dob = f'{dob.day} {dobmonth} {dob.year}'

        dob = Label(root, text='Date of Birth  : ' + dob, bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        dob.place(x=400, y=230)

        age = Label(root, text='Age Group     : ' + str(details[3]), bg='LightSkyBlue1', fg='black', font=('Times new roman', 14), wraplength=0)
        age.place(x=400, y=270)

        details_tup = [('Member Id', details[0], 'Name', details[1]),
                           ('Contact no.', details[4], 'Age', details[3]),
                           ('DOB', details[2], 'DOR', details[10])]

        butt = Button(root, text = "Exit", padx = 20, pady = 10, command = root.destroy)
        butt.pack(side = 'bottom')

        root.mainloop()

