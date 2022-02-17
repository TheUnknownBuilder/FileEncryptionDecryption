import copy
import tkinter as tk
from button import HoverButton
from tkinter import *
from tkinter import filedialog
import shutil
import datetime as dt
import os
import ProgramVar as pv
import ntpath
import fileencrypt

# class mainmenu:
#     	def __init__(self, name, player_type):
# 		self.name = name
# 		self.player_type = player_type

ntpath.basename("a/b/c")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

filename=''
def Menu():
    root = tk.Tk()
    #root.bind ('<Return>', enterCallback)

    frame = tk.Frame (root, padx=20, pady=20, bg="#2C3A57")
    frame.grid (row=0, column=0, sticky='news')
    
    # frame=tk.Frame(root, padx=20, pady=20, bg="#2C3A57")
    # frame.grid(row=1, column=0,sticky='news')
    pass_var=tk.StringVar
    pass_var.set("")
    
    intro = tk.Label (frame, text="Encryption and Decryption of Files", wraplength=800,
                      font=("Calibri", 15), bg = "#2C3A57", fg = "white")
    Upload1 = tk.Label (frame, text="Upload your file", font=("Calibri", 9), bg = "#2C3A57", fg = "white")
    passLabel = tk.Label (frame, text="Password", font=("Calibri", 9), bg = "#2C3A57", fg = "white") #need to put * there
    passwordBox = tk.Entry(frame, width=20, bg = "#A3A3B1", show="*", textvariable=pass_var) 
    # passLabel2 = tk.Label (frame, text="Confirm Password", font=("Calibri", 9), bg = "#2C3A57", fg = "white") #need to put * there
    password1=pass_var.get()
    # passwordBox2 = tk.Entry(frame, width=20, bg = "#A3A3B1", show="*")
    #Download1=tk.Label (frame, text="Download your file", font=("Calibri", 9), bg = "#2C3A57", fg = "white")
    
    def Decrypt(password):
        newfilename=path_leaf(filename)
        newfilename="assets\\"+ newfilename
        fileencrypt.decrypt(newfilename,password)
        
        
    def Encrypt(password):
        newfilename = path_leaf(filename)
        copyReportFile(newfilename)
        newfilename="assets\\"+ newfilename
        fileencrypt.encrypt(newfilename,password)
        print("Encryption Done")
        
    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("Text files",
                                                                "*.pdf*"),
                                                            ("Image files",
                                                                "*.png*"),
                                                            ("Image files",
                                                                "*.jpeg*"),
                                                            ("Text files",
                                                                "*.txt*")))
        label_file_explorer = Label(frame,
                                text = "File Explorer",
                                width = 75, height = 2,
                                fg = "grey")
        
        label_file_explorer.configure(text="File Opened: "+filename)
        
        label_file_explorer.grid(row=2, column=1)
        # button_submit = tk.Button(frame,
        #                 text = "Submit", command=copyReportFile)
        # button_submit.grid(column = 0,row = 5, columnspan=2)

# Set window title

    def copyReportFile (newfilename):
        # source folder
        global filename
        # source filename
        name = filename[filename.rfind('/')+1 : len(filename)]

        # destination folder
        newdir = pv.pdfPath
        # destination filename

        newpath = newdir + '\\' + newfilename

        shutil.copy2 ((filename), newdir)
        os.rename ((newdir+ '\\' +name), (newdir+ '\\' +newfilename))
        

    encrypt1= HoverButton(frame,text="Encrypt", activebackground='#3fc0cc', font=("Bahnschrift", 9),command=lambda: Encrypt("password1"))
    decrypt1= HoverButton(frame,text="Decrypt", activebackground='#3fc0cc', font=("Bahnschrift", 9),command=lambda: Decrypt("password1"))
    browse=tk.Button(frame, text='Browse Files',activebackground='#3fc0cc', font=("Bahnschrift", 9),command=browseFiles )
        
    intro.grid (row=0, column=0, columnspan=2)
    encrypt1.grid(row=4, column=0)
    decrypt1.grid(row=4, column=1)
    Upload1.grid (row=1, column=0,columnspan=2)
    browse.grid(row=2, column=0)
    passLabel.grid (row=3, column=0)
    passwordBox.grid (row=3, column=1)
    #Download1.grid(row=5, column=0)
    
    root.columnconfigure (0, weight=1, minsize=500)
    root.rowconfigure (0, weight=1, minsize=300)
    # root.rowconfigure (1, weight=1, minsize=300)
    
 
    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)
    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    frame.rowconfigure (4, weight=1)
    frame.rowconfigure (5, weight=1)
    
    # frame.columnconfigure (0, weight=1)
    # frame.columnconfigure (1, weight=1)
    # frame.rowconfigure (0, weight=1)
    # frame.rowconfigure (1, weight=1)
    # frame.rowconfigure (2, weight=1)
    # frame.rowconfigure (3, weight=1)
    # frame.rowconfigure (4, weight=1)
    # frame.rowconfigure (5, weight=1)


    root.mainloop ()
    

if __name__ == '__main__':
    Menu ()