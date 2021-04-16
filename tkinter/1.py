import tkinter

window = tkinter.Tk()

window.title("todo_list") #창 이름
window.geometry("640x400+100+100") #창 크기
window.resizable(False, False)# 창 조정 가능성 여부

label = tkinter.Label(window, text='안녕하세요', width=10, height=5, fg='red', relief='solid')
label.pack()

window.mainloop()