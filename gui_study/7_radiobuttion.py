from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x480")    # "가로 x 세로"

Label(root, text="Select Menu").pack()

# Radiobutton : 여러개 중에서 하나만 선택
burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheezeburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="Select Drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Cider", value="Cider", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())    # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()