import mysql.connector
from tkinter import *
from functools import partial
from tkinter import messagebox
from tabulate import tabulate
from cfonts import render, say
import sys 

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nidhikarkera0",database="library")
mycursor=mydb.cursor()


output = render('GreyStone Library',size = (100, 10), align='center')
print()
print()
print(output)
print()
print()
print("\t\t\t====================================================")
#tkinter login

root = Tk()  
root.geometry('325x150')  
root.title('Login Form')
root.configure(bg='#5093C7')

lib_user = "Admin"
lib_pass = "pythonlol"
failed_attempt_counter = 0

def login(userid, passw):
        try:
                global failed_attempt_counter
                a  = False
                while not(a):
                        userid = username.get()
                        passw = password.get()
                        if userid == lib_user and passw == lib_pass:
                                messagebox.showinfo("Message", "Log in successful!")
                                root.destroy()
                                while True:
                                        print()
                                        print("\t\t\t\t\t\tMAIN MENU")
                                        print("\t\t\t\t\t========================")
                                        print()
                                        table=[["1. Registration for Members/Add a book"],
                                                ["2. Search for books/members"],
                                                ["3. Issue or Return Books"],
                                                ["4. Update Records"],
                                                ["5. Reports"],
                                                ["6. Exit"]]
                                                            
                                        headers=["OPTIONS"]
                                        print(tabulate(table,headers,tablefmt="fancy_grid"))

                                        print()         
                                        choice = input("Enter your choice: ")
                                        print("\t\t\t====================================================")
                                        if choice=='1':
                                                import registerfinal
                                                print("\t\t\t====================================================")
                                        elif choice=='2':
                                                import searchfinal
                                                print("\t\t\t====================================================")
                                        elif choice=='3':
                                                import issuereturnfinal
                                                print("\t\t\t====================================================")
                                        elif choice=='4':
                                                import updateordeletefinal
                                                print("\t\t\t====================================================")
                                        elif choice=='5':
                                                import reportfinal
                                                print("\t\t\t====================================================")
                                        elif choice=='6':
                                                a=True
                                                print("\t\t\t\t\t   KEEP READING!")
                                                break
                                                
                                        else:
                                                print("Enter a valid choice!")
                                                        
                        else:
                                stat = False
                                while not(stat):
                                        print("Authentication failed!", "Try again!")
                                        failed_attempt_counter += 1
                                        if failed_attempt_counter >= 3:
                                                print("Exceeded max attempts! Only three attempts allowed.")
                                                root.destroy()
                                                stat = True
                                                sys.exit()
                                                return
                                        else:
                                                return
        except:
                print("Error! Try again!")
                
            

                                    
user = Label(root, text = "Username").place(x = 50, y = 20) #username entry
username = StringVar()
username_entry = Entry(root, textvariable=username).place(x = 150, y = 20)

passwd = Label(root, text = "Password").place(x = 50, y = 60)#password entry
password = StringVar()
password_entry = Entry(root, textvariable=password, show='*').place(x = 150, y = 60)

login = partial(login, username, password)


button = Button(root, text="Log in", command = login).place(x = 145, y = 100)
root.quit()

root.mainloop()


#except:
#    print("Try again!")
    
