import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"


values = [str(i)+"일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")    # 최초 목록 제목 설정 / 버튼 클릭을 통한 값 설정 가능


readonly = ttk.Combobox(root, height=10, values=values, state="readonly")    # 읽기 전용
readonly.current(0)    # 0번째 index값 선택
readonly.pack()


def btncmd():
    print(combobox.get())    # 선택된 값 표시
    print(readonly.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()