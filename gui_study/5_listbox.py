from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"

listbox = Listbox(root, selectmode="extended", height=0)
# extended : 여러개 선택 / single : 한개만 선택
# height : 지정된 수 만큼 리스트목록이 보여짐. 0이면 전부 보여짐.

listbox.insert(0, "apple")
listbox.insert(1, "lemon")
listbox.insert(2, "grape")
listbox.insert(END, "banana")    # END : 리스트박스 맨 뒤에 값 추가
listbox.insert(END, "strawberry")
listbox.pack()

def btncmd():
    # 삭제, delete(index)
    listbox.delete(END)

    # 갯수 확인
    print(f"리스트에는 {listbox.size()}개가 있음")

    # 항목 확인, get(시작idx, 끝idx)
    print(f"1부터 3까지의 항목 :", listbox.get(0, 2))

    # 선택된 항목 확인, index 반환
    print("Selected :", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()