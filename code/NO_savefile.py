# importing all files from tkinter
from importlib.resources import files
from tkinter import *
from tkinter import ttk

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile
#from code.fileencrypt import encrypt
import fileencrypt

root = Tk()
root.geometry('200x150')

# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file1=asksaveasfile(filetypes = files, defaultextension = files, title='Download the file',mode='w')
 

data=fileencrypt.encrypt('assets\grade-3-roman-numerals-read-1-50-a.pdf_encrypted_decrypted.pdf')
file=open(file1, 'w')
file.write(data)
file.close()
    
btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack(side = TOP, pady = 20)

mainloop()
