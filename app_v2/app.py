import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import Entry, StringVar, Button, Label, messagebox, ttk, Tk
from redactor import DocxRedactor
import os

window = Tk()
window.title("REDACTOR")
window.geometry("400x480")

def choose_file():
    global fileName
    fileName.set(askopenfilename())

def redact_file():
    filepath, fileExtension = os.path.splitext(fileName.get())
    fullredactedpath = filepath + "_" + postfixEntry.get() + fileExtension
    
    redactor = DocxRedactor(fileName.get(), [regexEntry.get()], replacementCharacterEntry.get())
    redactor.redact(fullredactedpath)

TitleFont = "Calibri 20 bold1"
labelFont = "Calibri 16 bold"
labelHintFont = "Calibri 11"

appTitle = Label(window, text="REDACTOR", font=("Calibri 24 bold"))
appTitle.place(x=202, y=32, anchor="center")

chooseFileButton = tk.Button(window,text="Choose a file", width=50, font=("Calibri 14"),command=choose_file)
chooseFileButton.place(x=20, y=80, anchor="w", height="35")

fileName = StringVar(window, "No file selected.")
fileNameLabel = Label(window,textvariable=fileName,font=(labelHintFont))
fileNameLabel.place(x=15,y=110, anchor="w")

postfixLabel = Label(window, text="POSTFIX", font=(labelFont))
postfixLabel.place(x=15, y=135, anchor="w")

postfixLabelHint = Label(window, text="It will append to the original file name. i.e. yourDoc_redacted.docx", font=(labelHintFont))
postfixLabelHint.place(x=15, y=155, anchor="w")

postfixEntry = Entry(window, width=39, highlightbackground="#dddddd", highlightthickness="1", border="0")
postfixEntry.insert(0, "redacted")
postfixEntry.pack()
postfixEntry.place(x=20, y=185, anchor="w", height=35)

regexLabel = Label(window, text="REGEX", font=(labelFont))
regexLabel.place(x=15, y=230, anchor="w")

regexLabelHint = Label(window, text="Tell us what to capture", font=(labelHintFont))
regexLabelHint.place(x=15, y=250, anchor="w")

regexEntry = Entry(window, width=39, highlightbackground="#dddddd", highlightthickness="1", border="0")
regexEntry.insert(0, "\[(.*?)\]")
regexEntry.pack()
regexEntry.place(x=20, y=280, anchor="w", height=35)

replacementCharacterLabel = Label(window, text="REPLACEMENT CHARACTER", font=(labelFont), textvariable="hello")
replacementCharacterLabel.place(x=15, y=325, anchor="w")

replacementCharacterEntry = Entry(window, width=39, highlightbackground="#dddddd", highlightthickness="1", border="0")
replacementCharacterEntry.insert(10, "x")
replacementCharacterEntry.pack()
replacementCharacterEntry.place(x=20, y=358, anchor="w", height=35)

redactButton = Button(window, text="REDACT",  width=39, background="#000", font=("Calibri 16 bold"), command=redact_file)
redactButton.place(x=20, y=420, anchor="w", height="35")

window.mainloop()