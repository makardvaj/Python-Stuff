import mysql.connector
My_DB = mysql.connector.connect(host = 'localhost',
                                user = 'root',
                                passwd = '12345678',
                                database = 'LIBRARY')

def Add_Book() :
    Title = input("Enter Book Title : ")
    Author = input("Enter Author's Name : ")
    ISBN = input("Enter ISBN : ")
    Genre = input("Enter Genre : ")
    Copies = int(input("Number Of Copies : "))
    Row = (Title, Author, ISBN, Genre, Copies)
    Query = '''INSERT INTO BOOKS VALUES(%s, %s, %s, %s, %s);'''
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query, Row)
    My_DB.commit()
    print("\nBook ", ISBN, " added succesfully!\n")
    Pause = input("\nPress ENTER to continue...\n")
    main()

def Issue_Book() :
    Name = input("Enter Student Name : ")
    Adm_No = int(input("Enter Admission Number : "))
    ISBN = input("Enter ISBN : ")
    Date = input("Enter Date : ")
    Query = '''INSERT INTO ISSUED_BOOKS VALUES(%s,%s,%s,%s,%s);'''
    Row = (Name, Adm_No, ISBN, Date)
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query, Row)
    My_DB.commit()
    print("\nBook ", ISBN, " issued successfully to student ",Adm_No,".")
    Pause = input("\nPress ENTER to continue...\n")
    Update_Book(ISBN, -1)
    main()

def Return_Book() :
    Name = input("Enter Student Name : ")
    Adm_No = int(input("Enter Admission Number : "))
    ISBN = input("Enter book code : ")
    Date = input("Enter Date : ")
    Query = "INSERT INTO RETURNED BOOKS VALUES(%s,%s,%s,%s,%s);"
    Row = (Name, Adm_No, ISBN, Date)
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query, Row)
    My_DB.commit()
    print("\nBook ", ISBN, " returned by student ",Adm_No,".")
    Pause = input("\nPress ENTER to continue...\n")
    Update_Book(ISBN, 1)
    main()

def Update_Book(ISBN, Increament) :
    Query = "SELECT TOTAL FROM BOOKS WHERE ISBN = %s;"
    Row = (ISBN,)    # tuple of Query single element requires comma
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query, Row)
    My_Result = My_Cursor.fetchone()
    Total = My_Result[0] + Increament
    New_Query = "UPDATE BOOKS SET COPIES = %s WHERE ISBN = %s;"
    New_Row = (Total, ISBN)
    My_Cursor.execute(New_Query, New_Row)
    My_DB.commit()
    Pause = input("\nPress ENTER to continue...\n")
    main()

def Delete_Book() :
    ISBN = int(input("Enter Book Code : "))
    Query = "DELETE FROM BOOKS WHERE ISBN = %s;"
    Row = (ISBN,)
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query, Row)
    My_DB.commit()
    print("\nBook ", ISBN, "deleted succesfully!\n")
    Pause = input("\nPress ENTER to continue...\n")
    main()

def Display_Books() :
    Query = "SELECT * FROM BOOKS;"
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query)
    My_Result = My_Cursor.fetchall()
    for i in My_Result :
        print("Title : ", i[0])
        print("Author : ", i[1])
        print("ISBN : ", i[2])
        print("Subject : ", i[3])
        print("Copies :", i[4])
        print()
    Pause = input("\nPress ENTER to continue...\n")
    main()

def Generate_Issued_Books_Report() :
    Query = "SELECT * FROM ISSUED_BOOKS"
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query)
    My_Result = My_Cursor.fetchall()
    for i in My_Result :
        print(My_Result)
    Pause = input("\nPress ENTER to continue...\n")
    main()

def Generate_Returned_Books_Report() :
    Query = "SELECT * FROM RETURNED_BOOKS;"
    My_Cursor = My_DB.cursor()
    My_Cursor.execute(Query)
    My_Result = My_Cursor.fetchall()
    for i in My_Result :
        print(My_Result)
    Pause = input("\nPress ENTER to continue...\n")
    main()

def main() :
    print("*"+('=' * 40)+"*")
    print("*"+(' ' * 40)+"*")
    print("*     LIBRARY MANAGEMENT APPLICATION     *")
    print("   ====================================   ")
    print("*"+(' ' * 40)+"*")
    print("*   1. Add A Book                        *")
    print("*   2. Issue A Book                      *")
    print("*   3. Return A Book                     *")
    print("*   4. Delete A Book                     *")
    print("*   5. Display A Book's Details          *")
    print("*   6. Generate A Report                 *")
    print("*   7. Exit The Program                  *")
    print("*"+(' ' * 40)+"*")
    print("*"+('=' * 40)+"*")
    print()
   
    Choice = input("Enter Task no. : ")
    print()
    if Choice == '1' :
        Add_Book()
    elif Choice == '2' :
        Issue_Book()
    elif Choice == '3' :
        Return_Book()
    elif Choice == '4' :
        Delete_Book()
    elif Choice == '5' :
        Display_Books()
    elif Choice == '6' :
        print('''
        REPORT MENU
        ===========

        1. ISSUED BOOKS
        2. RETURNED BOOKS
        3. NEITHER (RETURN TO MAIN MENU)
        \n''')

        New_Choice = input("Enter Secondary Task Number : ")
        print()
        if New_Choice == '1' :
            Generate_Issued_Books_Report()
        elif New_Choice == '2' :
            Generate_Returned_Books_Report()
        elif New_Choice == '3' :
            main()
        else :
            print("\n[INVALID INPUT] Please try again!\n")
            main()
    elif Choice == '7' :
        print("\nExiting...\n")
        exit
    else :
        print("\n[INVALID INPUT] Please try again!\n")
        main()

main()
