import tkinter as tk
from getDataFromDB import getData
from tkinter import ttk

fini_name_cate = getData()

class PyWinDesign:
    def __init__(self, 启动窗口):
        self.启动窗口 = 启动窗口
        self.启动窗口.title('豆瓣评论信息爬取与分析')
        self.启动窗口.resizable(width=False, height=False)
        screenwidth = self.启动窗口.winfo_screenwidth()
        screenheight = self.启动窗口.winfo_screenheight()
        size = '%dx%d+%d+%d' % (645, 433, (screenwidth - 645) / 2, (screenheight - 433) / 2)
        self.启动窗口.geometry(size)

        self.photo = tk.PhotoImage(file='../Douban_Comments_Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments_WC.png')
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=208, y=224, width=381, height=191)

        self.编辑框1 = tk.Text(self.启动窗口, wrap=tk.NONE,font=("宋体", 18, "bold"))
        self.编辑框1.insert(tk.END, '解忧杂货店')
        self.编辑框1.place(x=263, y=14, width=125, height=35)

        self.编辑框2 = tk.Text(self.启动窗口, wrap=tk.WORD,font=("宋体", 14, "bold"))
        with open('../Douban_Comments_Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments.txt','r',encoding='gbk') as f:
            text = f.read()
        self.编辑框2.insert(tk.END, text)
        self.编辑框2.place(x=205, y=58, width=429, height=149)


        self.超级列表框1 = ttk.Treeview(self.启动窗口, show='headings', columns=(['已完成的任务']))
        self.超级列表框1.column('已完成的任务',width=100,anchor='center')
        self.超级列表框1.heading('已完成的任务', text='已完成的任务')

        finished = fini_name_cate.keys()
        i = 0
        #print(finished)
        for name in finished:
            if ' ' in name:
                name = name.replace(" ","_")
            self.超级列表框1.insert('',i,values=name)
            i+=1
        self.超级列表框1.place(x=15, y=53, width=119, height=343)

        self.超级列表框1.bind("<<TreeviewSelect>>",self.hello)

    def hello(self,event):
        clic = event.widget.selection()[0][-1:]     # 取出16进制
        seq = int(clic,16)
        clic_name = list(fini_name_cate)[seq-1:seq][0]
        clic_cate = list(fini_name_cate.values())[seq-1:seq][0]

        self.编辑框1.delete(1.0, "end")    # 先删后改
        self.编辑框1.insert(tk.END, clic_name)

        imgPath = '../Douban_Comments_Spider/comments_infor/{}/{}/{}_comments_WC.png'.format(clic_cate,clic_name,clic_name)
        self.photo = tk.PhotoImage(file=imgPath)
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=208, y=224, width=381, height=191)

        textPath = '../Douban_Comments_Spider/comments_infor/{}/{}/{}_comments.txt'.format(clic_cate,clic_name,clic_name)
        with open(textPath,'r',encoding = 'gbk') as f:
            clic_text = f.read()
        self.编辑框2.delete(1.0, "end")     # 先删后改
        self.编辑框2.insert(tk.END, clic_text)


if __name__ == '__main__':
    root = tk.Tk()
    app = PyWinDesign(root)
    root.mainloop()