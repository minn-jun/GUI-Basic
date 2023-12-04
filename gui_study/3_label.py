from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")

label1 = Label(root, text="hi")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you later")
    
    # Garbage Collection : 불필요한 메모리 공간 해제
    # 전역변수가 아닌 경우 photo2값을 지울 수 있음
    global photo2    # 함수 내에서 label의 이미지를 변경할 경우 전역변수로 설정
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()