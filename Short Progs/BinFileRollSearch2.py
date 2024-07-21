# Create a binary file with roll number, name and marks. Input a roll number and update the marks.

import pickle

Binary_File = open("Desired_Path.bat", mode = 'wb')

n = int(input("Enter number of entries to be written : "))
for i in range(n) :
    Roll_No = input(f"Enter roll number {i+1} : ")
    Name = input("Enter name {i+1} : ")
    Marks = float(input("Enter marks {i+1} : "))
    Array = tuple([Roll_No, Name, Marks])
    pickle.dumb(Array, Binary_File)
    print()

Binary_File.close()

File = open("Desired_Path.bat", mode = 'rb')

New_Arrays = []

print("\nProcedding to the searching section.\n")

r = input("Enter roll number to search for : ")
Text = pickle.load(File)
for Record in Text :
    if Record[0] == r :
        New_Marks = float(input(f"New marks for #{r} : "))
        New_Record = [r, Record[1], New_Marks]
        New_Array = tuple(New_Record)
    else :
        New_Record = Record
        New_Array = tuple(New_Record)
    New_Arrays.append(New_Array)      

File.close()
