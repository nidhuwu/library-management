import mysql.connector
from tabulate import tabulate  
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nidhikarkera0',database='library')
mycursor=mydb.cursor()
    

def search_bookid():
    try: 
        print()
        BookID=int(input("Enter the Book ID: "))
        mycursor.execute("select * from books where BookID={}".format(BookID))
        result=mycursor.fetchall()
        if result==[]:
            print("Book not found!")
            print()
        else:
            print(tabulate(result,headers = ['Book ID','Book name','Author','Date of Publication',
                                     'Genre','Rating','No of copies','Price'],tablefmt='fancy_grid'))
            print()
    except:
        print()
        print("Error! Try again!")
        
def search_bookname():
    try:
        print()
        Bookname = input("Enter the Book name: ")
        mycursor.execute(f"select * from books where Name = '{Bookname}'") #you might have saved your column name as Bookname, so change that
        result=mycursor.fetchall()
        if result==[]:
            print("Book not found!")
            print()
        else:
            print(tabulate(result,headers = ['Book ID','Book name','Author','Date of Publication',
                                     'Genre','Rating','No of copies','Price'],tablefmt='fancy_grid'))
            print()
    except:
        print()
        print("Error! Try again!")
        
def search_bookgenre():
    try:
        print()
        genre=input("Enter the genre: ")
        mycursor.execute(f"select * from books where genre='{genre}'")
        result=mycursor.fetchall()
        if result==[]:
            print("Book not found!")
            print()
        else:
            print(tabulate(result,headers=['Book ID','Book name','Author','Date of Publication',
                                     'Genre','Rating','No of copies','Price'],tablefmt='fancy_grid'))
            print()
    except:
        print()
        print("Error! Try again!")
        


def search_memID():
    try:
        print()
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
        
    except:
        print()
        print("Error! Try again!")
        
def search_memName():
    try:
        print()
        Name=input("Enter Member name: ")
        mycursor.execute(f"select * from members where Name='{Name}'")
        result=mycursor.fetchall()
        if result==[]:
            print("Member not found!")
            print()
        else:
            print(tabulate(result,headers=['Member ID', 'Name','Date of Birth','Age',
                                     'Contact','Block no','Bldg no','Road no','Flat no',
                                     'Area','Date of Registration','Fine Charges'],tablefmt='fancy_grid'))
            print()
        
    except:
        print()
        print("Error! Try again!")

def search_memcontact():
    try:
        print()
        contact=input("Enter the contact number: ")
        mycursor.execute(f"select * from members where contact='{contact}'")
        result=mycursor.fetchall()
        if result==[]:
            print("Member not found!")
            print()
        else:
            print(tabulate(result,headers=['Member ID', 'Name','Date of Birth','Age',
                                         'Contact','Block no','Bldg no','Road no','Flat no',
                                         'Area','Date of Registration','Fine Charges'],tablefmt='fancy_grid'))
            print()
            
    except:
        print()
        print("Error! Try again!")
        
#SUB MENU
print()
print("\t\t\t\t\t\t SEARCH")

while True:
    try:
        print("\t\t\t\t\t========================")
        print()
        print('''Search for a 
    1. Member
    2. Book
    3. Back to the Main Menu''')
        print()
        choice= input("Enter your choice: ")
        print("==================")
        if choice == '1':	
            while True:
                print('''Search member by: 
    1. Member ID
    2. Member name
    3. Contact number
    4. Back to menu''')
                print()
                opt = input("Enter your choice: ")
                
                if opt == '1':
                    search_memID()
                    
                elif opt == '2':
                    search_memName()

                elif opt == '3':
                    search_memcontact()
                elif opt == '4':
                    break

                else:
                    print()
                    print("Enter a valid option!")
                    print()
                    
        elif choice == '2':
            while True:
                print('''Search book by: 
    1. Book ID
    2. Book name
    3. Genre
    4. Back to menu''')
                print()
                ch = input("Enter your choice: ")
                
                if ch == '1':
                    search_bookid()
                    
                elif ch == '2':
                    search_bookname()
                    
                elif ch == '3':
                    headers = ['Choose a genre']
                    t = [["Fantasy"], ["Young adult fiction"],
                        ["Historical fiction"],  ["Romance novel"],
                        ["Children's fiction"], ["Fictional autobiography"],
                        ["Fantasy fiction"],["Science fiction"],
                        ["Southern gothic fiction"], ["Political fiction"],
                        ["Modernism"]]
                    print(tabulate(t, headers, tablefmt = 'fancy_grid'))
                    search_bookgenre()
                elif ch == '4':
                        break
                else:
                    print()
                    print("Enter a valid option!")
                    print()
                    
        elif choice == '3':
            break
        
        else:
            print()
            print("Enter a valid option!")
            print()

    except:
        print("Error! Try again!")
        
    
        
    
