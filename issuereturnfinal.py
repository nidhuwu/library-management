import mysql.connector
import datetime
from datetime import date, timedelta
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nidhikarkera0", database="library")
mycursor=mydb.cursor()

def Issue():
        print("Issuing...")
        print()
        bid = int(input("Enter the Book ID: "))
        mycursor.execute(f"select * from books where BookID = {bid};")
        result=mycursor.fetchall()
                                
        if result==[]:
                print("Book is not available!")
                print()
        else:  #To check if the book has already been issued
                mycursor.execute(f"select * from issuereturn where BookID={bid} and MemID={MemID} and Status='Issued';")
                result1=mycursor.fetchall()
                if result1==[]:
                        mycursor.execute("update books set Number_of_books=Number_of_books-1 where BookID={};".format(bid))
                        mydb.commit()
                                
                        d1=datetime.date.today() 
                        d2=d1+timedelta(weeks=2)  
                        mycursor.execute("select Name from members where MemID={};".format(MemID))
                                
                        Name=str(mycursor.fetchall()[0][0])
                        mycursor.execute("select Name from books where BookID={}".format(bid))
                        BookName=str(mycursor.fetchall()[0][0])
                        conlist=[[Name,BookName,d1,d2]]
                                
                        print(tabulate(conlist,headers=['Member Name','Book name','Issue Date','Return Date'],tablefmt='fancy_grid'))
                        print()
                        option=input("Do you confirm the issue? [Y/N)]: ")
                        print()
                        if option in "yY":
                                q1="update issuereturn set Status='Issued' where BookID = {} and MemID = {} and Issue_Date='{}'".format(bid,MemID,d1)
                                query="insert into issuereturn(MemID,Name,BookID,BookName,Issue_Date,Return_Date,Fine_Charged)values(%s,%s,%s,%s,%s,%s,%s)"
                                record=(MemID,Name,bid,BookName,d1,d2,0)
                                mycursor.execute(query,record)
                                mycursor.execute(q1)
                                mydb.commit()
                        
                                mycursor.execute("""select MemID, BookID, Issue_Date, Return_Date, Status from
        issuereturn where Status='Issued' and MemID='{}' and BookID='{}'and Issue_Date='{}';""".format(MemID,bid,d1))
                                result=mycursor.fetchall()
                                print("Book Issued!")
                                print(tabulate(result,headers=['MemID', 'BookID','Issue Date','Return Date','Status'],tablefmt='fancy_grid'))
                                print()
                                        
                        elif option in "Nn":
                                print("Try again!")
                                print()
                        else:
                                print("Enter a valid option!")
                                
                else:
                        print("This book has already been issued.")
                        print()

def dates(test1,test2):
        y1,m1,d1=test1.split('-') 
        y1=int(y1)
        m1=int(m1)
        d1=int(d1)
                                 
        y2,m2,d2=test2.split('-')
        y2=int(y2)
        m2=int(m2)
        d2=int(d2)
        day1=date(y1,m1,d1)
        day2=date(y2,m2,d2)
        return(day2-day1).days
                
def Return():
        print("Returning...")
        print()
#        try:
        bid=input("Enter the Book ID: ")
        cd=input("Enter today's date [YYYY-MM-DD]: ")                               
        finamt=0 
        mycursor.execute("select Return_Date from issuereturn where MemID='{}' and BookID='{}' and Status='Issued'".format(MemID,bid))
        result=mycursor.fetchall()
                    
        if str(result[0][0])<str(cd):
                price=mycursor.execute(f"select price_of_books from books where BookID={bid};")
                price=float(mycursor.fetchall()[0][0])
                rdate=str(result[0][0])
                cdate=str(cd)
                ndays=dates(rdate,cdate)
                finamt=(price*0.5)*ndays
                
        else:
                finamt==0

        mycursor.execute("update books set Number_of_books=Number_of_books+1 where BookID='{}'".format(bid))
        mydb.commit()
                            
        mycursor.execute("update members set Fine_Charges=Fine_Charges+'{}' where MemID='{}'".format(finamt,MemID))
        mydb.commit()
                            
        mycursor.execute("select MemID,Name,Fine_Charges from members where MemID='{}'".format(MemID))
        result=mycursor.fetchall()
                            
        rd=str(datetime.date.today())
        print("Fine charged =",finamt)
        print("Book Returned!")
        print(tabulate(result,headers=['MemID', 'Name','Total Fine Charged'],tablefmt='fancy_grid'))
        mycursor.execute("update issuereturn set Status='Returned',Returned_Date='"+rd+"',Fine_Charged='"+str(finamt)+"' where MemID='"+str(MemID)+"' and BookID='"+str(bid)+"'and Status='Issued'")
        mydb.commit()
                
#        except:
#                print("Error! Try Again!")

print()
print("\t\t\t\t\t ISSUE AND RETURN BOOKS")
while True:
        print("\t\t\t\t\t========================")
        print('''1. To issue a book
2. To return a book
3. Back to Main menu''')
        print()
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
                MemID=int(input("Enter the Member ID: "))
                print()
                mycursor.execute("select * from members where MemID='{}'".format(MemID))
                result=mycursor.fetchall()
                if result==[]:
            #incase the memid entered is not registered with the library
                    print("Member not found!")
                    print()
        
                else:
                #to display the details of the books he/she has been issued with
                        mycursor.execute("select * from issuereturn where MemID='{}'".format(MemID))
                        result=mycursor.fetchall()
                
                        if result==[]:
                                print("No books issued!")
                                print()
                                Issue()
                    
                        else:    #if they've been issued count how many books they're currently issued with
                                mycursor.execute("select count(*) from issuereturn where Status='Issued' and MemID='{}'".format(MemID))
                                result=mycursor.fetchall()
                                for k in result: #a maximum of 5 books can be issued at a time to a member
                                        for j in k:
                                                if j>=5:
                                                        print("Maximum number of books have been issued!")
                                                        break
                                        else:
                                                mycursor.execute("select MemID,BookID,Issue_Date,Return_Date from issuereturn where Status='Issued' and MemID='{}'".format(MemID))
                                                result=mycursor.fetchall()
                                                if result==[]:
                                                        print("Member has returned all books.")
                                                        print()
                                                        Issue()
                                                else:
                                                        print(tabulate(result,headers=['MemID', 'BookID','IssueDate','ReturnDate','Status'],tablefmt='fancy_grid'))
                                                        print()
                                                        Issue()
        #Returning Books part
        elif choice == '2':
                MemID = input("Enter the Member ID: ")
                print()
                mycursor.execute("select * from members where MemID='{}'".format(MemID))
                result=mycursor.fetchall()
                if result==[]:
            #incase the memid entered is not registered with the library
                        print("Member not found!")
                else:
                        mycursor.execute("select MemID,BookID,Issue_Date,Return_Date,Status from issuereturn where Status='Issued' and MemID='{}'".format(MemID))
                        result=mycursor.fetchall()
                        if result==[]:
                                print("Member has returned all the books.")
                                print()
                        
                        else:
                                print(tabulate(result,headers=['MemID', 'BookID','IssueDate','ReturnDate','Status'],tablefmt='fancy_grid'))
                                print()
                                Return()
        elif choice == '3':
                break
        
        else:
                print("Enter a valid choice!")
                print()
