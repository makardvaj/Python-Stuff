# Remove all the lines that contain the character 'a' in a file and write it to another file.

New_Lines = []

Read_File = open("Path_Of_File_To_Be_Read.txt", mode = 'r')
Text = Read_File.readlines()
for Line in Text :
    if Line[0] == 'a' :
        New_Lines.append(Line)
    else :
        continue
Read_File.close()

Written_File = open("Path_Of_File_To_Be_Written_To.txt", mode = 'w')
for New_Line in New_Lines :
    Written_File.write(New_Line)
Written_File.close()
