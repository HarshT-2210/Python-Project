# project Banking system :
import mysql.connector as a

try :
    conn = a.connect(host="localhost",user="root",password="",database="Bank")
except Exception as e:
    print("Not connected to Database")
else:
    print("Successfully connected to Database")
    main()

# first to insert details and open account :
def openAcc():
    n=input("Enter your Name : ")
    ac=int(input("Enter Account Number : "))
    db=input("Enter Date Of Birth : ")
    m=int(input("Enter Mobile No. : "))
    addr=input("Enter Address location : ")
    ob=float(input("Enter Opening balance : "))
    data1 = (n,ac,db,m,addr,ob)
    data2 = (n,ac,ob)
    query1 = "insert into account values(%s,%s,%s,%s,%s,%s)"
    query2 = "insert into amount values(%s,%s,%s)"

    c = conn.cursor() # create a cursor to run query
    c.execute(query1,data1)
    c.execute(query2,data2)
    conn.commit()
    print("Data Entered Successfully")
    main()

# to deposit amount in account :
def depositAmt():
    am=float(input("Enter Amount to deposit : "))
    ac=int(input("Enter Account number : "))
    query1 = "select balance from amount where acno = %s"
    data1 = (ac,)
    c = conn.cursor()
    c.execute(query1,data1)
    result = c.fetchone()
    total_amt = result[0] + am
    query2 = "update amount set balance = %s where acno = %s"
    data2 = (total_amt,ac)
    c.execute(query2,data2)
    conn.commit()
    print("Amount Deposited Successfully")
    main()

# to withdraw amount from account :
def withDraw():
    am=float(input("Enter Amount to Withdraw : "))
    ac=int(input("Enter Account number : "))
    query1 = "select balance from amount where acno = %s"
    data1 = (ac,)
    c=conn.cursor()
    c.execute(query1,data1)
    result = c.fetchone()
    total_amt = result[0] - am
    query2 = "update amount set balance = %s where acno = %s"
    data2 = (total_amt,ac)
    c.execute(query2,data2)
    conn.commit()
    main()

# to show balance from the account :
def balance():
    ac=int(input("Enter Account number : "))
    query1 = "select balance from amount where acno = %s"
    data1 = (ac,)
    c=conn.cursor()
    c.execute(query1,data1)
    result = c.fetchone()
    print("Balance amount for Account : ",ac," is ",result[0])
    main()     

# to display account details from bank :
def displayAcc():
    ac=int(input("Enter Account number : "))
    query1 = "select * from account where acno = %s"
    data1 = (ac,)
    c = conn.cursor()
    c.execute(query1,data1)
    result = c.fetchone()
    for i in result:
        print(i)
    main()

# to close/delete account permenantly :
def closeAcc():
    ac=int(input("Ente Account number : "))
    query1 = "delete from account where acno = %s"
    query2 = "delete from amount where acno = %s"
    data = (ac,)
    c = conn.cursor()
    c.execute(query1,data)
    c.execute(query2,data)
    conn.commit()
    main()


def main():
    print('''
    1. TO OPEN NEW ACCOUNT
    2. TO DEPOSIT AMOUNT
    3. TO WITHDRAW AMOUNT
    4. TO ENQUIRE BALANCE
    5. TO DISPLAY ACCOUNT DETAILS
    6. TO CLOSE ACCOUNT
    7. TO ABORT THE TASKS
    ''')
    choice = input("Enter Task to perform : ")
    while True:
        if (choice=="1"):
            openAcc()
        elif (choice=="2"):
            depositAmt()
        elif (choice=="3"):
            withDraw()
        elif (choice=="4"):
            balance()
        elif (choice=="5"):
            displayAcc()
        elif (choice=="6"):
            closeAcc()
        else:
            print("You chose to Abort the Task")
            print("Do you want to continue to Abort Task ? : yes(Y)/No(N)")
            choice = input("yes=y/no=n : ")
            if (choice=="n"):
                 main()
            elif (choice=="y"):
                print("Task Aborted Successfully")
                try:
                    conn.close()
                except Exception as e:
                    print("Connection not closed")
                else:
                    print("Connection closed successfully")
                break
        break
        print("Thank You")


            
            
            
            














