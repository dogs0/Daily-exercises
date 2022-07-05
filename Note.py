import tkinter as tk
from tkinter import scrolledtext
import os

def save(evt=None):
    filename=note_title.get()
    content=note_content.get(0.0,'end')
    if os.path.isfile(filename+'.note.txt'):
        if open(filename+'.note.txt','r',encoding='utf-8').read() == content[:-1]:
            return 0
        with open(filename+'.note.txt','w',encoding='utf-8') as fileio:
            fileio.write(content[:-1])
        with open(filename+' - 副本.note.txt','w',encoding='utf-8') as fileio:
            fileio.write(content[:-1])
    return 0

def add_new_note(evt=None):
    save()
    note_title.delete(0,'end')
    note_content.delete(0.0,'end')

def on_close(evt=None):
    save()
    root.destroy()

def regularly_save(evt=None):
    if os.path.isfile(note_title.get()):
        thefile=open(note_title.get(),'r',encoding='utf-8')
        thefilecont=thefile.read()
        thecont=note_content.get(0.0,'end')
        if thefilecont not in thecont and thecont not in thefilecont:
            return 

    if note_content.get(0.0,'end') != '\n':
        save()
    root.after(300000,regularly_save)

def open_file(evt=None):
    filename=note_title.get()
    content=note_content.get(0.0,'end')
    note_content.delete(0.0,'end')
    print(filename)
    if os.path.isfile(filename+'.note.txt'):
        with open(filename+'.note.txt','r',encoding="utf-8") as fileio:
            note_content.delete(0.0,'end')
            note_content.insert(0.0,fileio.read())
        with open('temp.note.txt','w',encoding='utf-8') as push:
            push.write(content)

root=tk.Tk()
root.wm_attributes('-topmost',True)
root.geometry("300x400")
root.resizable(False,False)
root.protocol('WM_DELETE_WINDOW',on_close)

button1=tk.Button(root,text='创建新笔记',command=add_new_note)
button1.place(x=0,y=0,width=300,height=30)
note_title=tk.Entry(root)
note_title.place(x=0,y=30,width=300,height=30)
note_content=scrolledtext.ScrolledText(root)
note_content.place(x=0,y=60,width=300,height=340)

root.after(300000,regularly_save)
note_title.bind("<KeyRelease>",open_file)

root.mainloop()
