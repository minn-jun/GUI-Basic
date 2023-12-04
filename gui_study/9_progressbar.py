import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)    # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()    # 작동 중지

# btn = Button(root, text="click", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()    # 실수 반영
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)    # progressbar의 값 설정
        progressbar2.update()    # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()