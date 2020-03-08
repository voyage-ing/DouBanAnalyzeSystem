import tkinter as tk
from tkinter import ttk

from getDataFromDB import getData
fini_name_cate = getData()


class PyWinDesign:
    def __init__(self, 启动窗口):
        self.启动窗口 = 启动窗口
        self.启动窗口.title('豆瓣评论信息爬取与分析')
        self.启动窗口.resizable(width=False, height=False)
        screenwidth = self.启动窗口.winfo_screenwidth()
        screenheight = self.启动窗口.winfo_screenheight()
        size = '%dx%d+%d+%d' % (904, 509, (screenwidth - 904) / 2, (screenheight - 509) / 2)
        self.启动窗口.geometry(size)

        self.photo = tk.PhotoImage(file='../Douban-Comments-Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments_WC.png')
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=160, y=238, width=419, height=268)

        self.编辑框2 = tk.Text(self.启动窗口, wrap=tk.NONE)
        with open('../Douban-Comments-Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments.txt', 'r', encoding='gbk') as f:
            text = f.read()
        self.编辑框2.insert(tk.END,text)
        self.编辑框2.place(x=156, y=60, width=460, height=165)

        self.超级列表框1 = ttk.Treeview(self.启动窗口, show='headings', columns=(['已完成的任务']))
        self.超级列表框1.column('已完成的任务', width=100, anchor='center')
        self.超级列表框1.heading('已完成的任务', text='已完成的任务')

        finished = fini_name_cate.keys()
        i = 0
        # print(finished)
        for name in finished:
            if ' ' in name:
                name = name.replace(" ", "_")
            self.超级列表框1.insert('', i, values=name)
            i += 1
        self.超级列表框1.place(x=5, y=60, width=121, height=386)
        self.超级列表框1.bind("<<TreeviewSelect>>", self.clickLs)  # 绑定事件

        self.按钮1_标题 = tk.StringVar()
        self.按钮1_标题.set('|')
        self.按钮1 = tk.Button(self.启动窗口, textvariable=self.按钮1_标题)
        self.按钮1.place(x=639, y=0, width=6, height=512)

        self.按钮2_标题 = tk.StringVar()
        self.按钮2_标题.set('------'*20)
        self.按钮2 = tk.Button(self.启动窗口, textvariable=self.按钮2_标题)
        self.按钮2.place(x=154, y=227, width=482, height=8)

        self.按钮4_标题 = tk.StringVar()
        self.按钮4_标题.set('----'*100)
        self.按钮4 = tk.Button(self.启动窗口, textvariable=self.按钮4_标题)
        self.按钮4.place(x=-2, y=48, width=907, height=5)

        self.标签2_标题 = tk.StringVar()
        self.标签2_标题.set('新建豆瓣对象')
        self.标签2 = tk.Label(self.启动窗口, textvariable=self.标签2_标题)
        self.标签2.place(x=689, y=8, width=175, height=34)

        self.选择框2_选中 = tk.IntVar()
        self.选择框2_选中.set(0)
        self.选择框2_标题 = tk.StringVar()
        self.选择框2_标题.set('是否启用代理IP')
        self.选择框2 = tk.Checkbutton(self.启动窗口, textvariable=self.选择框2_标题, variable=self.选择框2_选中, onvalue=1, offvalue=0)
        self.选择框2.place(x=644, y=64, width=120, height=27)

        self.编辑框5 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框5.insert(tk.END, '启用代理IP')
        self.编辑框5.place(x=710, y=94, width=189, height=22)

        self.选择框3_选中 = tk.IntVar()
        self.选择框3_选中.set(0)
        self.选择框3_标题 = tk.StringVar()
        self.选择框3_标题.set('是否启用Headers')
        self.选择框3 = tk.Checkbutton(self.启动窗口, textvariable=self.选择框3_标题, variable=self.选择框3_选中, onvalue=1, offvalue=0)
        self.选择框3.place(x=644, y=131, width=130, height=23)

        self.编辑框8 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框8.insert(tk.END, '启用Headers')
        self.编辑框8.place(x=710, y=159, width=189, height=22)

        self.标签4_标题 = tk.StringVar()
        self.标签4_标题.set('请输入爬取对象名称：')
        self.标签4 = tk.Label(self.启动窗口, textvariable=self.标签4_标题, anchor=tk.W)
        self.标签4.place(x=656, y=199, width=120, height=31)

        self.编辑框9 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框9.insert(tk.END, '新建的名字')
        self.编辑框9.place(x=708, y=234, width=190, height=24)

        self.标签5_标题 = tk.StringVar()
        self.标签5_标题.set('请输入爬取对象类型：')
        self.标签5 = tk.Label(self.启动窗口, textvariable=self.标签5_标题, anchor=tk.W)
        self.标签5.place(x=657, y=271, width=125, height=29)

        self.编辑框10 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框10.insert(tk.END, '("movie","music","book")')
        self.编辑框10.place(x=708, y=302, width=190, height=23)

        self.按钮7_标题 = tk.StringVar()
        self.按钮7_标题.set('-----------------------------------------------------------')
        self.按钮7 = tk.Button(self.启动窗口, textvariable=self.按钮7_标题)
        self.按钮7.place(x=642, y=344, width=264, height=5)

        self.标签6_标题 = tk.StringVar()
        self.标签6_标题.set('确认信息无误点击提交：')
        self.标签6 = tk.Label(self.启动窗口, textvariable=self.标签6_标题, anchor=tk.W)
        self.标签6.place(x=656, y=365, width=146, height=31)

        self.按钮8_标题 = tk.StringVar()
        self.按钮8_标题.set('提交新建对象')
        self.按钮8 = tk.Button(self.启动窗口, textvariable=self.按钮8_标题)
        self.按钮8.place(x=789, y=425, width=105, height=44)

        self.标签7_标题 = tk.StringVar()
        self.标签7_标题.set('解忧杂货店(book)')
        self.标签7 = tk.Label(self.启动窗口, textvariable=self.标签7_标题,font=("宋体", 20, "bold"))
        self.标签7.place(x=228, y=9, width=236, height=29)

        self.标签8_标题 = tk.StringVar()
        self.标签8_标题.set('当前豆瓣对象:')
        self.标签8 = tk.Label(self.启动窗口, textvariable=self.标签8_标题, anchor=tk.E)
        self.标签8.place(x=110, y=13, width=108, height=23)

        self.按钮9_标题 = tk.StringVar()
        self.按钮9_标题.set('↓')
        self.按钮9 = tk.Button(self.启动窗口, textvariable=self.按钮9_标题)
        self.按钮9.place(x=611, y=59, width=17, height=166)

    def clickLs(self,event):
        clic = event.widget.selection()[0][-1:]  # 取出16进制
        seq = int(clic, 16)
        clic_name = list(fini_name_cate)[seq - 1:seq][0]
        clic_cate = list(fini_name_cate.values())[seq - 1:seq][0]

        # 改豆瓣对象名字
        self.标签7_标题.set('{}({})'.format(clic_name,clic_cate))

        # 改图片
        imgPath = '../Douban-Comments-Spider/comments_infor/{}/{}/{}_comments_WC.png'.format(clic_cate, clic_name,clic_name)
        self.photo = tk.PhotoImage(file=imgPath)
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=160, y=238, width=419, height=268)

        # 改评论信息
        textPath = '../Douban-Comments-Spider/comments_infor/{}/{}/{}_comments.txt'.format(clic_cate, clic_name,clic_name)
        with open(textPath, 'r', encoding='gbk') as f:
            clic_text = f.read()
        self.编辑框2.delete(1.0, "end")  # 先删后改
        self.编辑框2.insert(tk.END, clic_text)


if __name__ == '__main__':
    root = tk.Tk()
    app = PyWinDesign(root)
    root.mainloop()