File = open("FILE_PATH.txt", mode = 'r')
Text = File.read()
# A 65 Z 90   a 97 z 122

Count_Consonants = 0
Count_Uppercase_Consonants = 0
Count_Lowercase_Consonants = 0

Count_Vowels = 0
Count_Uppercase_Vowels = 0
Count_Lowercase_Vowels = 0

Count_Letters = 0
Count_Uppercase_Letters = 0
Count_Lowercase_Letters = 0

Count_Digits = 0
Count_Punctuation = 0
Count_Spaces = 0
Count_Miscellaneous = 0

for Character in Text :
    if 65 <= ord(Character) <= 90 :
        Count_Letters += 1
        Count_Uppercase_Letters += 1
        if Character in ('A', 'E', 'I', 'O', 'U') :
            Count_Uppercase_Vowels += 1
            Count_Vowels += 1
        else :
            Count_Uppercase_Consonants += 1
            Count_Consonants += 1
    elif 97 <= ord(Character) <= 122 :
        Count_Letters += 1
        Count_Lowercase_Letters += 1
        if Character in ('a', 'e', 'i', 'o', 'u') :
            Count_Lowercase_Vowels += 1
            Count_Vowels += 1
        else :
            Count_Lowercase_Consonants += 1
            Count_Consonants += 1
    elif Character in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') :
        Count_Digits += 1
    elif Character in ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~') :
        Count_Punctuation += 1
    elif Character == ' ' :
        Count_Spaces += 1
    else :
        Count_Miscellaneous += 1

File.close()

print(f"The file contains {Count_Letters + Count_Digits + Count_Punctuation + Count_Spaces + Count_Miscellaneous} characters, in total.\n\nThere are {Count_Letters} letters in the file.\nOut of those, {Count_Lowercase_Letters} are lowercase.\nAnd, {Count_Uppercase_Letters} are uppercase.\n\nThere are {Count_Consonants} consonants in the file.\nOut of those, {Count_Lowercase_Consonants} are lowercase.\nAnd, {Count_Uppercase_Consonants} are uppercase.\n\nThere are {Count_Vowels} vowels in the file.\nOut of those, {Count_Lowercase_Vowels} are lowercase.\nAnd, {Count_Uppercase_Vowels} are uppercase.\n\nThere are {Count_Digits} digits in the file.\nThere are {Count_Punctuation} punctuation marks in the file.\nThere are {Count_Spaces} spaces in the file.\nThere are {Count_Miscellaneous} miscellaneous characters in the file.\n\n")
