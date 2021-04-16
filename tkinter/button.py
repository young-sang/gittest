import tkinter

window=tkinter.Tk()
window.title('hello')
window.geometry('640x400+100+100')
window.resizable(False, False)

count = 0

def countup():
    global count
    count +=1
    label.config(text=str(count))

label = tkinter.Label(window, text='0')
label.pack()

button = tkinter.Button(window, overrelief='solid', width=15, command=countup, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()