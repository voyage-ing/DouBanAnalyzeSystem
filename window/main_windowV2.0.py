import tkinter as tk
from tkinter import ttk
import requests
from getDataFromDB import getData
from faker import Factory
from tkinter import messagebox
import os,sys
sys.path.append('/Users/hang/PycharmProjects/bishe/Douban_Comments_Spider')

# MySQL库中数据引入
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

        self.photo = tk.PhotoImage(file='../Douban_Comments_Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments_WC.png')
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=160, y=238, width=419, height=268)

        self.编辑框2 = tk.Text(self.启动窗口, wrap=tk.NONE)
        with open('../Douban_Comments_Spider/comments_infor/book/解忧杂货店/解忧杂货店_comments.txt', 'r', encoding='gbk') as f:
            text = f.read()
        self.编辑框2.insert(tk.END,text)
        self.编辑框2.config(highlightbackground="black",highlightcolor="blue",highlightthickness=2)
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
        # # 创建勾选项
        # c1 = tk.Checkbutton(window, text='人工智能',
        #                     variable=var1,
        #                     onvalue=1,  # 勾选中该项时，把1放入var1
        #                     offvalue=0,  # 不勾选中该项时，把０放入var1
        #                     command=print_selection,             # 点击勾选调用的函数
        #                     )
        self.选择框2 = tk.Checkbutton(self.启动窗口, textvariable=self.选择框2_标题, variable=self.选择框2_选中, onvalue=1, offvalue=0,command=self.useProxy)
        self.选择框2.place(x=644, y=64, width=120, height=27)

        self.编辑框5 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框5.insert(tk.END, '(点击选择框启用代理IP)')
        self.编辑框5.config(highlightbackground="green",highlightcolor="blue",highlightthickness=2)
        self.编辑框5.place(x=710, y=94, width=189, height=22)

        self.选择框3_选中 = tk.IntVar()
        self.选择框3_选中.set(0)
        self.选择框3_标题 = tk.StringVar()
        self.选择框3_标题.set('是否启用Headers')
        self.选择框3 = tk.Checkbutton(self.启动窗口, textvariable=self.选择框3_标题, variable=self.选择框3_选中, onvalue=1, offvalue=0,command=self.useUA)
        self.选择框3.place(x=644, y=131, width=130, height=23)

        self.编辑框8 = tk.Text(self.启动窗口, wrap=tk.NONE)
        self.编辑框8.insert(tk.END, '(点击选择框启用Headers)')
        self.编辑框8.config(highlightbackground="green",highlightcolor="blue",highlightthickness=2)
        self.编辑框8.place(x=710, y=159, width=189, height=22)



        self.标签4_标题 = tk.StringVar()
        self.标签4_标题.set('请输入爬取对象名称：')
        self.标签4 = tk.Label(self.启动窗口, textvariable=self.标签4_标题, anchor=tk.W)
        self.标签4.place(x=656, y=199, width=120, height=31)

        self.编辑框9 = tk.Text(self.启动窗口, wrap=tk.NONE,font=("宋体", 12, "bold"))
        self.编辑框9.config(highlightbackground="green",highlightcolor="blue",highlightthickness=2)
        self.编辑框9.insert(tk.END, '(新建爬取对象的名字)')
        # <Button-1>表示鼠标左键单击，其中的 1 换成 3 表示右 键被单击，为 2 的时候表示鼠标中键，感觉不算常用。
        self.编辑框9.bind('<Button-1>',self.deleteText)
        self.编辑框9.place(x=708, y=234, width=190, height=24)

        self.标签5_标题 = tk.StringVar()
        self.标签5_标题.set('请输入爬取对象类型：')
        self.标签5 = tk.Label(self.启动窗口, textvariable=self.标签5_标题, anchor=tk.W)
        self.标签5.place(x=657, y=271, width=125, height=29)

        self.编辑框10 = tk.Text(self.启动窗口, wrap=tk.NONE,font=("宋体", 12, "bold"))
        self.编辑框10.insert(tk.END, '("movie","music","book")')
        self.编辑框10.config(highlightbackground="green",highlightcolor="blue",highlightthickness=2)
        self.编辑框10.bind('<Button-1>',self.deleteText)
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
        self.按钮8.bind('<Button-1>',self.submit)
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
        clic = event.widget.selection()[0][-3:]  # 取出16进制
        seq = int(clic, 16)
        clic_name = list(fini_name_cate)[seq - 1:seq][0]
        clic_cate = list(fini_name_cate.values())[seq - 1:seq][0]

        # 改豆瓣对象名字
        self.标签7_标题.set('{}({})'.format(clic_name,clic_cate))

        # 改图片
        imgPath = '../Douban_Comments_Spider/comments_infor/{}/{}/{}_comments_WC.png'.format(clic_cate, clic_name,clic_name)
        self.photo = tk.PhotoImage(file=imgPath)
        self.图片1 = tk.Label(self.启动窗口, imag=self.photo, anchor=tk.CENTER)
        self.图片1.place(x=160, y=238, width=419, height=268)

        # 改评论信息
        textPath = '../Douban_Comments_Spider/comments_infor/{}/{}/{}_comments.txt'.format(clic_cate, clic_name,clic_name)
        try:
            with open(textPath, 'r', encoding='gbk') as f:
                clic_text = f.read()
        except:
            #  (U+0000-U+FFFF) 0-65535 ord()返回对应的 ASCII 数值，或者Unicode数值
            print('deal with SE')
            with open(textPath, 'r', encoding='UTF-8') as f:
                clic_text_origin = f.read()
            char_list = [clic_text_origin[j] for j in range(len(clic_text_origin)) if ord(clic_text_origin[j]) in range(65536)]
            clic_text = ''
            for j in char_list:
                clic_text = clic_text + j


        self.编辑框2.delete(1.0, "end")  # 先删后改
        self.编辑框2.insert(tk.END, clic_text)

    def useProxy(self):
        response = requests.get(url='http://127.0.0.1:5010/get/')
        proxy = eval(response.text)['proxy']
        self.编辑框5.delete(1.0,"end")
        self.编辑框5.insert(tk.END, proxy)
    def useUA(self):
        f = Factory.create()
        ua = f.user_agent()
        self.编辑框8.delete(1.0, "end")
        self.编辑框8.insert(tk.END, ua)

    def deleteText(self,event):
        tag = str(event.widget)[-1:]
        if tag == '4':
            self.编辑框9.delete(1.0,"end")
        else:
            self.编辑框10.delete(1.0,"end")

    def submit(self,event):
        # 第一个参数‘0.0’是指从第0行第0列开始读取（‘1.3’表示从第一行第3列开始读取），第二个参数End表示最后一个字符

        name = self.编辑框9.get("0.0","end").strip()
        sort = self.编辑框10.get("0.0","end").strip()
        #print(name +' ' + sort)

        if sort in ['book','music','movie']:
            messagebox.showinfo(title='提醒事项', message='{}：{}，创建成功！'.format(sort,name))

            from Douban_Comments_Spider.Start import start
            start(sort, name)
        else:
            messagebox.showinfo(title='无效的提交信息', message='ERROR！请确认对象信息输入后重新提交。')

if __name__ == '__main__':
    root = tk.Tk()
    app = PyWinDesign(root)
    root.mainloop()