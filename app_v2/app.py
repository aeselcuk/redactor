from tkinter.filedialog import askopenfilename
from tkinter import Tk
from tkinter import filedialog
from redactor import DocxRedactor
import os
import eel

eel.init('web')

def redact_file(file, postfix, regex, replacementChar):
    filepath, fileExtension = os.path.splitext(file)
    fullredactedpath = filepath + "_" + postfix + fileExtension
    
    redactor = DocxRedactor(file, [regex], replacementChar)
    redactor.redact(fullredactedpath)

@eel.expose
def btn_fileUpload():
	global filePath
	root = Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	filePath = filedialog.askopenfilename(filetypes=[("Word files", ".docx .doc")])

@eel.expose
def redact_py(webForm):
    redact_file(filePath, webForm["postfix"], webForm["regex"], webForm["replacementChar"])

eel.start('index.html')

    
