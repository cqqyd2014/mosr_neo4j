import tkinter        # 导入 Tkinter 库
root = tkinter.Tk()                     # 创建窗口对象的背景色


root.title("数据导入")
label = tkinter.Label(root,text="数据导入工具",width=100,height=10,anchor="n")

def showinfo():
    print(entry.get())

entry = tkinter.Entry(root)
entry.pack()
button = tkinter.Button(root, text="按钮", command=showinfo)
button.pack()
    
 
label.pack()                    # 将小部件放置到主窗口中

root.mainloop()   