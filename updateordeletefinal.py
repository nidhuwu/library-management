import datetime
from datetime import date
from tabulate import tabulate
import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(host='localhost', user ='root', passwd ='Nidhikarkera0', database ='library')
mycursor = mydb.cursor()

def age(birthdate):
    yy,mm,dd=birthdate.split('-')
    yy=int(yy)
    mm=int(mm)
    dd=int(dd)
    dob=date(yy,mm,dd)
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def Update_member():
    try:
        MemID=int(input("Enter the member ID: "))
        mycursor.execute("select * from members where MemID={}".format(MemID))
        result=mycursor.fetchall()
        if result==[]:
            print("Member not found!")
            print()
        else:
            print(tabulate(result,headers=['Member ID', 'Name','Date of Birth','Age',
                                     'Contact','Block no','Bldg no','Road no','Flat no',
                                     'Area','Date of Registration','Fine Charges'],tablefmt='fancy_grid'))
            print()
            while True:
                print('''
        Do you want to update -
            1. Name of the member
            2. Age of the member
            3. Address of the member
            4. Contact of the member
            5. Back to Menu
            ''') #options
                
                option = input("Enter your option: ")
                
                if option == "1": #Member name
                    try:
                        new_name = input("Enter the new name: ")
                        confirm = input(f'Confirmation: Name is being changed to {new_name} (Y/N): ')
                            
                        if confirm in 'Yy':
                            com = f"update members set Name = '{new_name}' where MemID = {MemID};"
                            mycursor.execute(com)
                            mycursor.execute(f'select * from members where MemID = {MemID} ;')
                            result=mycursor.fetchall()
                            print(tabulate(result,headers=['MemID','Name','Date of birth','Age',
                                                   'Contact','Block no','Bldg no','Road no','Flat no',
                                                   'Area','Date of Registration','Fine charges'],tablefmt='fancy_grid'))
                            mydb.commit()
                            print()
                            print("Member details have been updated!")
                                
                        elif confirm in 'Nn':
                            print("Name not changed!")     

                        else:
                            print("Try again!")
                            return
                            
                    except:
                        print("Error! Try again!")
                        return


                elif option == "2": #Member Age
                    try:
                        mycursor.execute("select date_of_birth from members where MemID='{}'".format(MemID))
                        date_of_birth=str(mycursor.fetchall()[0][0])
                        Age = age(date_of_birth)
                        confirm = input(f'Confirmation: Age is being changed to {Age} (Y/N): ')

                        if confirm in 'Yy':
                            mycursor.execute(f"update members set age = '{Age}' where MemID = {MemID};")
                            mycursor.execute(f'select * from members where MemID = {MemID} ;')
                            result=mycursor.fetchall()
                            print(tabulate(result,headers=['MemID','Name','Date of birth','Age',
                                               'Contact','Block no','Bldg no','Road no','Flat no',
                                               'Area','Date of Registration','Fine charges'],tablefmt='fancy_grid'))
                            mydb.commit()
                            print()
                            print("Member details have been updated!")
                        elif confirm in 'Nn':
                            print("Age not changed!")
                        else:
                            print("Try again!")
                            return
                        
                    except: 
                        print("Error! Try again!")
                        return
                    
                elif option == "3": #Member address
                    try:
                        Block = int(input("Enter the new block number: "))
                        bldg = int(input("Enter the new building number: "))
                        road = int(input("Enter the new road number: "))
                        Flat = int(input("Enter the new flat/house number: "))
                        Area = input("Enter the Area: ")
                        confirm = input(f'Confirmation: Address is being changed to block: {Block}, Bldg no: {bldg}, Road no: {road}, Flat/House no: {Flat}, Area: {Area} (Y/N): ')
                    
                        if confirm in 'Yy':
                            mycursor.execute(f"update members set Block_no = {Block}, Bldg_no = {bldg}, Road_no = {road},Flat_no = {Flat}, Area = '{Area}' where MemID = {MemID};")
                            mycursor.execute(f'select * from members where MemID = {MemID} ;')
                            result=mycursor.fetchall()
                            print(tabulate(result,headers=['MemID','Name','Date of birth','Age',
                                               'Contact','Block no','Bldg no','Road no','Flat no',
                                               'Area','Date of Registration','Fine charges'],tablefmt='fancy_grid'))
                            mydb.commit()
                            print()
                            print("Member details have been updated!")
                            
                        elif confirm in 'Nn':
                            print("Address not changed!")
                            
                        else:
                            print("Try again!")
                            return
                        
                    except:
                        print("Error! Try again!")
                        return
                        
                elif option == "4": #Member contact number
                    try: 
                        contact = input("Enter new contact number: ")
                        confirm = input(f'Confirmation: Contact is being changed to {contact} (Y/N): ')
                        
                        if confirm in 'Yy':
                            mycursor.execute(f"update members set Contact = '{contact}' where MemID = {MemID};")
                            mycursor.execute(f'select * from members where MemID = {MemID} ;')
                            result=mycursor.fetchall()
                            print(tabulate(result,headers=['MemID','Name','Date of birth','Age',
                                               'Contact','Block no','Bldg no','Road no','Flat no',
                                               'Area','Date of Registration','Fine charges'],tablefmt='fancy_grid'))
                            mydb.commit()
                            print()
                            print("Member details have been updated!")
                            
                        elif confirm in 'Nn':
                            print("Member details not changed!")
                            
                        else:
                            print("Try again!")
                            return
                    except:
                        print("Error! Try again!")
                        return
                


                elif option == "5":
                    break
                
                else: 
                    print("Enter a valid option!")

    except:
        print("Error! Try again")
        
def Update_book():

    BookID=int(input("Enter the Book ID: "))
    mycursor.execute("select * from books where BookID={}".format(BookID))
    result=mycursor.fetchall()
    
    print(tabulate(result,headers=['Book ID','Name','Author','Date of Publication',
                                   'Genre','Rating','Number of Copies','Price'],tablefmt='fancy_grid'))
    
    while True:
        print('''
Do you want to update -
    1. Rating of the book
    2. Price of the book
    3. No. of copies of the book
    4. Back to Menu
    ''') #options

        option = input("Enter your option: ")
        
        if option == "1": #Book Rating
            try:
                new_rating = input("Enter the new rating: ")
                confirm = input(f'Confirmation: Rating is being changed to {new_rating} (Y/N): ')
                    
                if confirm in 'Yy':
                    com = f"update books set rating = '{new_rating}' where BookID = {BookID};"
                    mycursor.execute(com)
                    mycursor.execute(f'select * from books where BookID = {BookID} ;')
                    result=mycursor.fetchall()
                    print(tabulate(result,headers=['Book ID','Name','Author','Date of Publication',
                                   'Genre','Rating',' Number of Copies','Price'],tablefmt='fancy_grid'))
    
            
                    mydb.commit()
                    print()
                    print("Book details have been updated!")
                        
                elif confirm in 'Nn':
                    print("Rating not changed!")     

                else:
                    print("Try again!")
                    return
                    
            except:
                print("Error! Try again!")
                return
        
        elif option == "2": #Book price
            try:
                new_price = input("Enter the new price: ")
                confirm = input(f'Confirmation: Price is being changed to {new_price} (Y/N): ')
                    
                if confirm in 'Yy':
                    com = f"update books set price_of_books = '{new_price}' where BookID = {BookID};"
                    mycursor.execute(com)
                    mycursor.execute(f'select * from books where BookID = {BookID} ;')
                    result=mycursor.fetchall()
                    print(tabulate(result,headers=['Book ID','Name','Author','Date of Publication',
                                   'Genre','Rating','Number of Copies','Price'],tablefmt='fancy_grid'))
    
            
                    mydb.commit()
                    print()
                    print("Book details have been updated!")
                        
                elif confirm in 'Nn':
                    print("Price not changed!")     

                else:
                    print("Try again!")
                    return
        
                    
            except:
                print("Error! Try again!")
                return
        elif option == "3": #Copies
            try:
                new_copies = input("Enter the number of copies: ")
                confirm = input(f'Confirmation: Number of Copies is being changed to {new_copies} (Y/N): ')
                    
                if confirm in 'Yy':
                    com = f"update books set Number_of_books = '{new_copies}' where BookID = {BookID};"
                    mycursor.execute(com)
                    mycursor.execute(f'select * from books where BookID = {BookID} ;')
                    result=mycursor.fetchall()
                    print(tabulate(result,headers=['Book ID','Name','Author','Date of Publication',
                                   'Genre','Rating','Number of Copies','Price'],tablefmt='fancy_grid'))
    
            
                    mydb.commit()
                    print()
                    print("Book details have been updated!")
                        
                elif confirm in 'Nn':
                    print("Number of copies not changed!")     

                else:
                    print("Try again!")
                    return
        
                    
            except:
                print("Error! Try again!")
                return
        elif option == "4": #returning to sub menu hehe
            break
        
        else: 
            print("Enter a valid option!")

    

            
def Deletemember():
    try:
        while True:
            MemID=int(input("Enter the member ID: "))
            mycursor.execute(f"select * from members where MemID={MemID}")
            result=mycursor.fetchall()
            if result==[]:
                print("Member not found!")
                break
            else:
                print(tabulate(result,headers=['MemID','Name','Date of birth','Age Group',
                                               'Contact','Block no','Bldg no','Road no','Flat no',
                                               'Area','Date of Registration','Fine charges'],tablefmt='fancy_grid'))
            mycursor.execute("select * from issuereturn where MemID='{}' and Status='Issued'".format(MemID))
            result1=mycursor.fetchall()
            if result1==[]:
                confirm =input("Are you sure you want to cancel this membership?(Y/N): ")
                try:
                    if confirm in "Yy":
                        query = f"delete from members where memid={MemID}"
                        mycursor.execute(query)
                        mydb.commit()
                        print("Membership successfully cancelled!")
                        break
                    elif confirm in "Nn":
                        print("Membership not cancelled.")
                        break
                    else:
                        print("Try again!")
                        return
                except:
                    print("Error! Try again!")
            else:
                print("This member has books pending to be returned, cancellation of membership is not possible.")
                print()
                break
                
    except:
        print("Error! Try again!")

print()            
print("\t\t\t\t\t     MANAGE RECORDS")
while True:
    print("\t\t\t\t\t========================")
    print()
    print('''Update details of:
1. A member
2. A book
3. Back to Main Menu
''')
    choice = input("Enter your choice: ")
    try:
        if choice == '1':
            while True:
                print()
                print('''1. Update Member details
2. Cancel Membership
3. Back to menu''')
                print()
                opt = input("Enter your choice: ")
                print()
                if opt == '1':
                    Update_member()
                elif opt == '2':
                    Deletemember()
                elif opt == '3':
                    break
                else:
                    print()
                    print("Enter a valid option!")
                    
        elif choice == '2':
                print()
                Update_book()
        elif choice == '3':
            break
        else:
            print()
            print("Enter a valid option!")
       
    except:
        print("Error! Try again!")
        break
