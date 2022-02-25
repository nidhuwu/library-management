
import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nidhikarkera0',database='library')
my_cursor=mydb.cursor()

def book_reports():      #book related reports
    my_cursor.execute("select * from books;")
    result=my_cursor.fetchall()
    print(tabulate(result,headers=['Book ID','Name','Author','Date of Publication',
                                   'Genre','Rating','No of copies','Price of Book'],tablefmt='fancy_grid'))
    

def member_reports():   #member related reports
    my_cursor.execute("select * from members;")
    result=my_cursor.fetchall()
    print(tabulate(result,headers=['Member ID','Name','Date of birth','Age','Contact','Block no',
                                   'Bldg no','Road no','Flat no','Area','Date of Registration','Fine Charges'],tablefmt='fancy_grid'))
    
def issue_return_reports():      #issue return related reports
    my_cursor.execute("select * from issuereturn;")
    result=my_cursor.fetchall()
    print(tabulate(result,headers=['MemID','Name','BookID','BookName','IssueDate','ReturnDate','Status','Returned Date','Fine Charged'],tablefmt='fancy_grid'))

print()            
print("\t\t\t\t\t\tRECORDS")
while True:
    print("\t\t\t\t\t========================")
    print()
    print('''1. Book Records
2. Member Records
3. Book Status Records
4. Back to Main Menu''')
    print()
    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            book_reports()
        except:
            print("Error! Try again!")
            
    elif choice == '2':
        try:
            member_reports()
        except:
            print("Error! Try again!")
    elif choice == '3':
        try:
            issue_return_reports()
    
        except:
            print("Error! Try again!")
    elif choice == '4':
        break
    
    else:
        print("Please enter a valid choice.")
        
            
            
