#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1.输入学习小时 分钟
2.在时间结束后窗口自动关闭

'''
import tkinter
import time
x, y = 0, 0
def main():
    def createTK1():
        def createTK2(totalTime, leftTime):
            while leftTime > 0:
                temp = leftTime
                sec = leftTime % 60
                temp //= 60
                min = temp % 60
                temp //= 60
                Time = "{:0>2}:{:0>2}:{:0>2}".format(str(temp), str(min), str(sec))
                canvas.create_text(150, 52, text=Time,fill="white")
                time.sleep(1)
                root.update()
                canvas.delete("all")
                leftTime -= 1

            root.destroy()

        def confirmEvent(event):
            if event.keysym == "Up":
                confirm()

        def confirm():
            if int(hour.get())<0 or int(min.get())<0:
                return
            totalTime = int(hour.get()) * 3600 + int(min.get()) * 60
            leftTime = totalTime
            canvas.delete("label1")
            root.update()
            createTK2(totalTime,leftTime)

        def move(event):
            global x, y
            new_x = (event.x - x) + root.winfo_x()
            new_y = (event.y - y) + root.winfo_y()
            s = "300x105+" + str(new_x) + "+" + str(new_y)
            root.geometry(s)
            '''
            print("s = ",s)
            print(root.winfo_x(),root.winfo_y())
            print(event.x,event.y)
            print()'''

        def button_1(event):
            global x, y
            x, y = event.x, event.y
            # print("event.x, event.y = ", event.x, event.y)

        root = tkinter.Tk()
        root.overrideredirect(True)
        root.attributes("-alpha", 0.8)  # 窗口透明度
        root.geometry("300x105+10+10")

        canvas = tkinter.Canvas(root)

        # canvas
        canvas.configure(width=300)
        canvas.configure(height=105)
        canvas.configure(bg="grey")
        canvas.configure(highlightthickness=0)
        canvas.pack()
        canvas.bind("<B1-Motion>", move)
        canvas.bind("<Button-1>", button_1)
        frm1 = tkinter.Frame(root)
        frm1.bind("<B1-Motion>", move)
        frm1.bind("<Button-1>", button_1)

        # frm1
        canvas.create_text(150,10,text = "请输入时间",fill="white")
        canvas.create_text(215,30,text = "hour",fill="white")
        canvas.create_text(220,55,text = "minute",fill="white")
        hour = tkinter.Entry(canvas)
        canvas.create_window((120, 30), window=hour)
        min = tkinter.Entry(canvas)
        canvas.create_window((120, 55), window=min)
        hour.bind("<KeyPress-Up>", confirmEvent)
        min.bind("<KeyPress-Up>", confirmEvent)
        button = tkinter.Button(canvas, text="确定", width=8, command=confirm)
        canvas.create_window((150, 86), window=button)

        root.wm_attributes('-topmost', 1)
        root.mainloop()

    createTK1()

if __name__ == '__main__':
    main()