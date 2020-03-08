from tkinter import *

myWindow = Tk()

# # window大小
# myWindow.geometry('800x500')

# 窗口大小放中间
width = 800
height = 500
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)

#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)

# 设置标题
myWindow.title('豆瓣评论信息爬取和分析')

# 设置菜单栏
menu = Menu(myWindow)
myWindow.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='Fileee',menu=filemenu)
menu.add_cascade(label='Edit',menu=filemenu)        # 有menu属性才会显示

filemenu.add_command(label='New',command='hello')

helpMenu = Menu(menu)
helpMenu.add_command(label='About')
menu.add_cascade(label='Help',menu=helpMenu)



# 布局设计
labeler = Label(myWindow,bg='blue',text="这里有个label")


labeler.pack(side=LEFT)
myWindow.mainloop()