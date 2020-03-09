import tkinter as tk
from tkinter import ttk

class AlterWin:
    def __init__(self, 启动窗口,sort,name):

        if sort == 'music':
            self.sort = '音乐'
        elif sort == 'book':
            self.sort = '书籍'
        else:
            self.sort = '电影'
        self.name = name

        self.启动窗口 = 启动窗口
        self.启动窗口.title('提醒事项')
        self.启动窗口.resizable(width=False, height=False)
        screenwidth = self.启动窗口.winfo_screenwidth()
        screenheight = self.启动窗口.winfo_screenheight()
        size = '%dx%d+%d+%d' % (427, 193, (screenwidth - 427) / 2, (screenheight - 193) / 2)
        self.启动窗口.geometry(size)

        self.标签1_标题 = tk.StringVar()
        self.标签1_标题.set('{}：{}，创建成功！'.format(self.sort,self.name))
        self.标签1 = tk.Label(self.启动窗口, textvariable=self.标签1_标题, anchor=tk.W,font=("宋体", 20, "bold"))
        self.标签1.place(x=39, y=17, width=343, height=97)

        self.按钮1_标题 = tk.StringVar()
        self.按钮1_标题.set('关闭')
        self.按钮1 = tk.Button(self.启动窗口, textvariable=self.按钮1_标题)
        self.按钮1.bind('<Button-1>',self.close)
        self.按钮1.place(x=301, y=139, width=86, height=33)


    def close(self,event):
        self.启动窗口.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = AlterWin(root,'music','name')
    root.mainloop()