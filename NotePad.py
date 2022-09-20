
from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def new():
    global file 
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)



def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All files","*.*"),
                                     ("Text file","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file == None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                         filetypes=[("All files","*.*"),
                                     ("Text file","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")

    else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()


def quitapp():
    root.destroy()

def copy():
    TextArea.event_generate(("<<Copy>>"))
def cut():
    TextArea.event_generate(("<<Cut>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","contact \nrohanshenoy29@gmail.com")

root=Tk()
root.title("Untitled - Notepad ") #to set the title of the window 
root.geometry("650x500") #dimension of the screen

#adding a scrollbar
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)


#adding a text area
TextArea=Text(root,font="lucida 13",yscrollcommand=scroll.set)
TextArea.pack(expand=True,fill=BOTH)
file=None


#adding a menu bar
MenuBar=Menu(root)

fileMenu=Menu(MenuBar,tearoff=0)
fileMenu.add_command(label="New",command=new)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitapp)

MenuBar.add_cascade(label="File",menu=fileMenu)


editMenu=Menu(MenuBar,tearoff=0)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=editMenu)


helpMenu=Menu(MenuBar,tearoff=0)
helpMenu.add_command(label="About",command=about)

MenuBar.add_cascade(label="Help",menu=helpMenu)

root.config(menu=MenuBar)

scroll.config(command=TextArea.yview)

root.mainloop()