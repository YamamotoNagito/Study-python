#codimg:utf-8
import tkinter as tk

def Buttonclick():

    height=float(height_box.get())
    weight=float(weight_box.get())
    bmi=weight/(height*height)

    bmi_box.delete(0,tk.END)
    bmi_box.insert(0,bmi)

    if bmi<18.5:
        result = "痩せ型"

    elif 18.5<=bmi<25:
        result = "標準体型"

    elif 25<=bmi:
        result = "肥満"

    result_box.delete(0,tk.END)
    result_box.insert(0,result)

#ウィンドウを作る
root=tk.Tk()
root.geometry("400x300")
root.title("BMI診断ツール")

#ラベルを作る
height_lavel=tk.Label(text="身長(m)")
height_lavel.place(x=60,y=50)

weight_lavel=tk.Label(text="体重(kg)")
weight_lavel.place(x=60,y=80)

bmi_lavel=tk.Label(text="BMI")
bmi_lavel.place(x=60,y=200)

result_lavel=tk.Label(text="あなたの体系は？")
result_lavel.place(x=50,y=240)

#テキストボックスを作る
height_box=tk.Entry(width=20)
height_box.place(x=140,y=50)

weight_box=tk.Entry(width=20)
weight_box.place(x=140,y=80)

bmi_box=tk.Entry(width=20)
bmi_box.place(x=140,y=200)

result_box=tk.Entry(width=20)
result_box.place(x=140,y=240)

#ボタンを作る
buttonl=tk.Button(root,text="診断する",font=("Halvetica",14),command=Buttonclick)
buttonl.place(x=140,y=130)

root.mainloop()
