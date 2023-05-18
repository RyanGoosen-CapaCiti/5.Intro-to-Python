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
import re
import subprocess

def get_default_program(extension):
    try:
        # Execute the command to query the default program for the extension
        command = ['xdg-mime', 'query', 'default', extension]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()

        # Decode the output and remove any trailing newline characters
        default_program = output.decode('utf-8').strip()
        
        return default_program
    except Exception as e:
        print("An error occurred:", str(e))

# Usage example

filename = input('Enter a file name: ') 
pattern = r'\.(\w+)$'

match = re.search(pattern, filename)

if match:
    extension_new = match.group(1)
    extension = extension_new
    default_program = get_default_program(extension)
    if default_program:
        print(f"The default program for opening .{extension} files is: {default_program}")
    else:
        print(f"No default program found for opening .{extension} files.")

else:
    print("No file extension found.")

