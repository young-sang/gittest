import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("to-do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!", message="you must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!", message="you must select a task")

def load_task():
    tasks1 = []
    with open("task.txt", "r", encoding='utf-8') as f:
        while True:
            line = f.readline()
            tasks1.append(line)
            if not line: break
            print(line)
        f.close
        del tasks1[-1:]
        
        tasks = tuple(tasks1)
        
    for task in tasks:
        listbox_tasks.insert(tkinter.END, tasks)

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("task.txt", "w", encoding='utf-8') as f:
        for line in tasks:
            f.write(line)


#create gui


frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="load task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="save task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()