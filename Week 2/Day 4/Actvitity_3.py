# Activity 3: This activity will be a dev team activity and will be graded.
# Time: 60 minutes
# Instructions
# Write a program that asks the user to input a file name. A message must be printed telling the user what kind of file it is and which software or application can be used to open the file based on its extension. Your program must be able to differentiate between 5 different file types.
# Output:
# >>> 
# Enter a file name: text.txt
# Text.txt is a Text Document and can be opened using a Notepad
# >>> 
# >>> =========== RESTART ======================
# >>> 
# Enter a file name: word.docx
# Word.docx is a Word Document and can be opened using MS Word
# >>> 
# >>> ============ RESTART ======================
# >>> 
name = input('Enter a file name: ') 
f = open(name, 'a')
print()
    # Check the different format you can open with, creating the document in write mode, need to write directly to the document after creation
f.write('0')
f.close()