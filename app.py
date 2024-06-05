import tkinter as tk 
from tkinter import*


def click():
    global textbox
    txt=textbox.get(1.0,"end-1c")
    if txt =="":
        pass
    else:
        #print(txt)
        lb = tk.Label(root,text=txt, width=40, height=2, bg="#74F476",anchor=W,wraplength=300,justify=LEFT)
        lb.pack(side=TOP, anchor=W, padx=15, pady=(10, 0))
        lb.config(font="Calibri 10")
        textbox.delete(1.0,END)

#Main Window
root =Tk()
root.minsize(450,600)
root.maxsize(450,600)
root.title("To Do List")
root.config(bg="#1B0E3C")

label1=tk.Label(root,text='All Tasks',fg='White',bg='#1B0E3C',font=("Arial",18,'bold'))
label1.pack(anchor=W,padx=15,pady=(10,0))

frame = tk.Frame(root, bg="#1B0E3C")
frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 15))

textbox=tk.Text(frame,bg="white",width=40,height=2)   #tk.Text is used for multilines inputs textbox
textbox.pack(side=LEFT,anchor=S,padx=(15,5),pady=(0,15))
textbox.config(padx=5,pady=5, font="calibri 10")


b=Button(frame,text="+",font="bold",width=2,height=1,bg='#788A8B',command=click)
b.pack(side=LEFT,anchor=S,padx=(5,5),pady=(0,23))


root.mainloop()