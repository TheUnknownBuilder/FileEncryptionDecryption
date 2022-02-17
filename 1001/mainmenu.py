import tkinter as tk
from button import HoverButton

def Menu():
    root = tk.Tk()
    #root.bind ('<Return>', enterCallback)

    frame = tk.Frame (root, padx=20, pady=20, bg="#2C3A57")
    frame.grid (row=0, column=0, sticky='news')

    intro = tk.Label (frame, text="Encyrption and Decryption of Files", wraplength=800,
                      font=("Calibri", 15), bg = "#2C3A57", fg = "white")
    Upload1 = tk.Label (frame, text="Upload your file", font=("Verdana", 9), bg = "#2C3A57", fg = "white")
    passLabel = tk.Label (frame, text="Password", font=("Verdana", 9), bg = "#2C3A57", fg = "white") #need to put * there
    # uName = tk.Entry(frame, width=20, bg = "#A3A3B1")
    passwordBox = tk.Entry(frame, width=20, bg = "#A3A3B1")
    Download1=tk.Label (frame, text="Download your file", font=("Verdana", 9), bg = "#2C3A57", fg = "white")

    encrypt1= HoverButton(frame,text="Encrypt", activebackground='#00BE00', font=("Bahnschrift", 9))
    decrypt1= HoverButton(frame,text="Decrpt", activebackground='#00BE00', font=("Bahnschrift", 9)
                           )

    intro.grid (row=0, column=0, columnspan=2)
    Upload1.grid (row=1, column=0)
    passLabel.grid (row=2, column=0)
    #uName.grid (row=1, column=1)
    passwordBox.grid (row=2, column=1)
    # login.grid (row=3, column=0)
    # register.grid (row=3, column=1)
    Download1.grid(row=3, column=0)
    encrypt1.grid(row=4, column=0)
    decrypt1.grid(row=4, column=1)

    root.columnconfigure (0, weight=1, minsize=500)
    root.rowconfigure (0, weight=1, minsize=300)

    frame.columnconfigure (0, weight=1)
    frame.columnconfigure (1, weight=1)
    frame.rowconfigure (0, weight=1)
    frame.rowconfigure (1, weight=1)
    frame.rowconfigure (2, weight=1)
    frame.rowconfigure (3, weight=1)
    # frame.rowconfigure (4, weight=1)

    root.mainloop ()

if __name__ == '__main__':
    Menu ()