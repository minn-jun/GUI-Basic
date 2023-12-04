from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 위로 올라옴
lstbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    lstbox.insert(END, str(i)+"일")

lstbox.pack(side="left")
scrollbar.config(command=lstbox.yview)

root.mainloop()