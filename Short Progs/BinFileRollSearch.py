# Create a binary file with name and roll number. Search for a given roll number and display the name, if not found, display appropriate message.

import pickle

# Opening a file in write(w) mode will automatically create the file, if it does not exist.
Binary_File = open("Desired_Path.dat", mode = 'wb')

n = int(input("Enter number of entries to be written : "))
for i in range(n) :
    Roll_No = input(f"Enter roll number {i+1} : ")
    Name = input("Enter name {i+1} : ")
    Array = tuple([Roll_No, Name])
    pickle.dumb(Array, Binary_File)
    print()

Binary_File.close()

File = open("Desired_Path.dat", mode = 'rb')
Choice = input("Data written; do you want to search the file? (Y/N)")

if Choice in ('Y', 'y') :
    Roll_No = input("Enter the roll number of the student : ")
    Data = pickle.load(Binary_File)
    for Record in Data :
        if Record[0] == Roll_No :
            print(Record[1])
            # Once found, no use in searching further.
            break
        else :
            continue
            
elif Choice in ('N', 'n') :
else :
    print("Invalid input!\n\nExiting program...")
    quit()

File.close()
