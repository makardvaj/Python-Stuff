# Create a CSV file by entering user-id and password, read and search the password for given userID

import csv

File = open("File_Path.csv", mode = "a+")
File_Writer = csv.writer(File)
File_Reader = csv.reader(File)

File_Writer.writerow(["UserID", "Password"])

n = int(input("How many entries do you want to store ?\n"))

for i in range(0, n) :
    UserID = input("Enter UserID {i+1} : ")
    Password = input("Enter Password {i+1} : ")
    File_Writer.writerow([UserID, Password])
    print()

UID = input("Enter the UserID to search for : ")
Data = File_Reader.read()
for Entry in Data :
    if Entry[0] == UID :
        print(f"The password of UserID {UID} is {Entry[1]} .")
        break
    else :
        continue

File.close()
