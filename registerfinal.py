import datetime
from datetime import date
from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nidhikarkera0',database='library')
my_cursor=mydb.cursor()

#registering a book
def add_book():
    try:
        PID=my_cursor.execute("select max(BookID) from books;")
        PID=int(my_cursor.fetchall()[0][0])
        BookID=PID+1

        print("Enter the following details")
        print()
        
        Bookname=input("Name of the book: ")
        Author=input("Name of the author: ")
        date_of_publication=input("Date of publication [YYYY-MM-DD]: ")
        genre=input("Genre of the book: ")
        rating=float(input("Rating of the book (out of 10): ")) #dont input a decimal number
        no_of_copies=int(input("Current number of copies of the book: "))
        price_of_books=float(input("Price of the book: ")) #float is fine
        rec=(BookID, Bookname, Author, date_of_publication, genre, rating, no_of_copies, price_of_books)
        rec1=[[BookID,Bookname,Author,date_of_publication,genre,rating,no_of_copies,price_of_books]]
        
        print(tabulate(rec1,headers=['Book ID','Book name','Author','Date of Publication',
                                     'Genre','Rating','No of copies','Price'], tablefmt = 'fancy_grid'))
        print()
        
        option=input("Do you confirm the registeration? [Y/N]: ")
        
        if option in "yY":
            query="insert into books(BookID, Name, Author, date_of_publication, genre,rating, no_of_copies, price_of_books) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            my_cursor.execute(query,rec)
            mydb.commit()
            print("Book registered!")
            
        elif option in "Nn":
            print("Registeration cancelled!")
            
        else:
            print("Try again!")
    except:
        print("Error! Try again!")

def age(birthdate):
    yy,mm,dd=birthdate.split('-')
    yy=int(yy)
    mm=int(mm)
    dd=int(dd)
    dob=date(yy,mm,dd)
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def add_member():
    try:
        PID=my_cursor.execute("select max(MemID) from members;")
        PID=int(my_cursor.fetchall()[0][0])
        MemID=PID+1

        print("Enter the following details")
        print()
        Name=input("Name of the member: ")
        
        date_of_birth=input("Date of birth [YYYY-MM-DD]: ")
        Age=age(date_of_birth)
        contact=int(input("Contact number of the member: "))
        print("Address")
        block_no=int(input("Block number: "))
        bldg_no=int(input("Building number: "))
        road_no=int(input("Road number: "))
        Flat_no=int(input("Flat/House number: "))
        Area=input("Area: ")
        Date_of_Registration=datetime.date.today()
        Fine_Charges=0
        
        rec=(MemID,Name,date_of_birth,Age,contact,block_no,bldg_no,road_no,Flat_no,Area,Date_of_Registration,Fine_Charges)
        rec1=[[MemID,Name,date_of_birth,Age,contact,block_no,bldg_no,road_no,Flat_no,Area,Date_of_Registration,Fine_Charges]]
        
        print(tabulate(rec1,headers=['Member ID', 'Name','Date of Birth','Age',
                                     'Contact','Block no','Bldg no','Road no','Flat no',
                                     'Area','Date of Registration','Fine Charges'],tablefmt='fancy_grid'))
        print()
        option = input("Do you confirm the registeration [Y/N]: ")
        
        if option in "yY":
            query="insert into members(MemID,Name,Date_of_birth,Age,Contact,Block_no,Bldg_no,Road_no,Flat_no,Area,Date_of_Registeration,Fine_Charges) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            my_cursor.execute(query,rec)
            mydb.commit()
            print("Member Registered!")
            
        elif option in "Nn":
            print("Registeration cancelled!")
            
        else:
            print("Try again!")
            
    except:
        print("Error! Try again!")


print()
print("\t\t\t\t\t\t REGISTER")
while True:
    print("\t\t\t\t\t========================")
    print()
    print('''1. Add a member
2. Add a book
3. View library cards
4. Back to the Main Menu''')

    print()
    choice = input("Enter your choice: ")
    print("==================")
    
    if choice == '1':
        try:
            add_member()
        except:
            print("Error! Try Again")
            
    elif choice == '2':
        try:
            add_book()
        except:
            print("Error! Try Again")
            
    elif choice == '3':
        try:
            import librarycardfinal
            librarycardfinal.mem_details()
        except:
            print("Error! Try Again")

    elif choice == '4':
        break
    
    else:
        print("Please enter a valid choice!")



















    












