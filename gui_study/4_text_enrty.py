from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"

# Text() : 메모장 느낌의 위젯
# 여러 줄 입력
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "insert text")


# Entry() : 생성된 위젯에서 텍스트 입력 시 줄바꿈(enter) 불가
# 한 줄로 입력을 받을 때
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄 입력")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))    # "1(line 1).0(column 0)", END(끝)
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()
root.mainloop()