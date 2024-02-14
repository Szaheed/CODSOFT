import tkinter
from tkinter import *

root = Tk()
root.title("To Do Lists")
root.geometry('320x550')
root.resizable(0,0)

task_lists=[]

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tsaklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_lists.append(task)
        listbox.insert( END , task)

def deleteTask():
    global task_lists
    task= str(listbox.get(ANCHOR))
    if task in task_lists:
        task_lists.remove(task)
        with open("tasklists.txt","w") as taskfile:
            for task in task_lists:
                taskfile.write(task+"\n")

    listbox.delete( ANCHOR)

def openTaskFile():

    try:
        global task_lists
        with open("tasklist.txt.txt","r") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task !='\n':
                    task_lists.append(task)
                    listbox.insert(END,task)

    except:
        file=open('tasklist.txt.txt','w')
        file.close()

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="black",bg="white")
heading.place(x=100,y=20)

frame=Frame(root,width=500,height=30,bg="white")
frame.place(x=0,y=120)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 15",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 13 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=250,y=0)


frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=32,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

Delete_icon=PhotoImage(file="Image/delete.png.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=1)

root.mainloop()