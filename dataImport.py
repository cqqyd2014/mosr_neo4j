from tkinter import *        # 导入 Tkinter 库




class App:
    def __init__(self, master):
        
        label_title = Label(root,text="数据导入工具")
        label_title.pack(side=TOP)
        #使用Frame增加一层容器
        main_frame = Frame(master)
        main_frame.pack(side=TOP)



 
        fm2 = Frame(master)
        f_control = Frame(fm2)
        f_control.grid(row=0, column=0)
        f_type=Frame(f_control)
        f_type.grid(row=0, column=0)
        l_type=Label(f_type, text='选择数据类型').pack()
        lb=Listbox(f_type, selectmode=SINGLE).pack()
        for item in ["MS SQL Server","Oracle","CSV"]:
            lb.insert(END, item)
        f_detail=Frame(f_control)
        f_detail.grid(row=1, column=0)
        b_test=Button(f_control, text='测试连接')
        b_test.grid(row=2, column=0)
        f_data_preview = Frame(fm2)
        f_data_preview.grid(row=1, column=0)
        

        fm2.pack(side=BOTTOM, fill=BOTH, expand=YES)




root = Tk()
root.title("数据导入")
root.geometry('300x200')
display = App(root)
root.mainloop()

