from tkinter import *

root = Tk()
root.geometry('400x250+500+300')
root.overrideredirect(True) 
TitleBar = Frame(root, bg = "#000000",relief="raised" ,bd=0,highlightthickness=0)
closeButton=Button(TitleBar,text=" X ",command=exit(),font="Calibri 10")
MaximizeButton=Button(TitleBar,text=" □ ",command=exit(),font="Calibri 10")
MinimizeButton=Button(TitleBar,text=" - ",command=exit(),font="Calibri 10")

window = Canvas(root,bg="#242424",highlightthickness=0)

TitleBar.pack(expand=1,fill=X)
closeButton.pack(side="RIGHT")
MaximizeButton.pack(side="RIGHT")
MinimizeButton.pack(side="RIGHT")
window.pack(expand=1,fill=BOTH)
root.mainloop()