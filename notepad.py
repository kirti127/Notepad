import tkinter
import os
from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import*

#create the class of notepad
class Notpad:
    __root=Tk()

#define the default width of the application
    __thiswidth=500
    __thisheight=500
#define the basic skelton of the application
    _thisTextArea=Text(__root)
    _thisMenuBar=Menu(__root)
    _thisFileMenu=Menu(_thisMenuBar,tearoff=0)
    _thisEditMenu=Menu(_thisMenuBar,tearoff=0)
    _thisHelpMenu=Menu(_thisMenuBar,tearoff=0)
    _thisScrollBar=Scrollbar(_thisTextArea)
    __file=None
#def center(self):
#   self.update_idletasks()
#  width = win.winfo_width()
#    height = win.winfo_height()
#    x = (win.winfo_screenwidth() // 2) - (width // 2)
#    y = (win.winfo_screenheight() // 2) - (height // 2)
#    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def __init__(self,**kwargs):
        self.__thisWidth=kwargs['width']
        self.__thisHeight = kwargs['height']
        self.__root.title("Untitled - Notepad")
        screenWidth=self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        x = (screenWidth/2)-(self.__thisWidth/2)
        y = (screenHeight/2)-(self.__thisHeight/2)
        self.__root.geometry('%dx%d+%d+%d'%(self.__thisWidth,self.__thisHeight, x, y))
        # to resize the text area automatically
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)
        self._thisTextArea.grid(sticky=N+E+S+W)
        self._thisFileMenu.add_command(label="New",command=self.__newFile)
        self._thisFileMenu.add_command(label="Open",command=self.__openFile)
        self._thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self._thisFileMenu.add_command(label="Save As...",command=self.__saveFileAs)
        self._thisFileMenu.add_separator()
        self._thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self._thisMenuBar.add_cascade(label="File",menu=self._thisFileMenu)
        self._thisEditMenu.add_command(label="Cut",command=self.__cut,accelerator="Ctrl+X")
        self._thisEditMenu.add_command(label="Copy",command=self.__copy,accelerator="Ctrl+C")
        self._thisEditMenu.add_command(label="Paste",command=self.__paste,accelerator="Ctrl+V")
        self._thisEditMenu.add_command(label="Select All",command=self.__selectAll,accelerator="Ctrl+A")
        self._thisMenuBar.add_cascade(label="Edit", menu=self._thisEditMenu)
        self._thisHelpMenu.add_command(label="About Notpad...",command=self.__showAbout)
        self._thisMenuBar.add_cascade(label="About", menu=self._thisHelpMenu)
        self.__root.config(menu=self._thisMenuBar)
        self._thisScrollBar.pack(side=RIGHT,fill=Y)
        self._thisScrollBar.config(command=self._thisTextArea.yview())
        self._thisTextArea.config(yscrollcommand=self._thisScrollBar.set)

 # to exit the application
    def __quitApplication(self):
        self.__root.destroy()
 #about notepad
    def __showAbout(self):
        showinfo("Notpad","Notpad Developed by:  KIRTI YADAV")
  # open file
    def __openFile(self):
        self.__file= askopenfilename(defaultextension="txt",
                          filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file=="":
           self.__file=None
        else:
            self.__root.title(os.path.basename(self.__file)+"-Notpad")
            self._thisTextArea.delete(1.0,END)
            file=open(self.__file,"r")
            self._thisTextArea.insert(1.0,file.read())
            file.close()
 # create a new file
    def __newFile(self):
        self.__root.title("Untitled- Notpad")
        self.__file=None
        self._thisTextArea.delete(1.0,END)
# save as
    def __saveFileAs(self):
        self.__file=asksaveasfilename(initialfile="*.txt",defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file=="":
            self.__file=None
        else:
            file=open(self.__file,"w")
            file.write(self._thisTextArea.get(1.0,END))
            file.close()
            self.__root.title(os.path.basename(self.__file)+"-Notpad")
    def __saveFile(self):
        if self.__file==None:
            self.__file = asksaveasfilename(initialfile="*.txt", defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.__file=="":
               self.__file=None
            else:
               file = open(self.__file, "w")
               file.write(self._thisTextArea.get(1.0, END))
               file.close()
               self.__root.title(os.path.basename(self.__file) + "-Notpad")
        else:

            file=open(self.__file,"w")
            file.write(self._thisTextArea.get(1.0,END))
            file.close()
    def __cut(self):
        self._thisTextArea.event_generate("<<Cut>>")
    def __copy(self):
        self._thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self._thisTextArea.event_generate("<<Paste>>")
    def __selectAll(self):
        self._thisTextArea.event_generate("<<Select All>>")
        self._thisTextArea.mark_set(INSERT,"1.0")
        self._thisTextArea.see(INSERT)
        return 'break'
    def run(self):
        self.__root.mainloop()
np = Notpad(width=1024,height=768)
np.run()