# -*- encoding=UTF-8 -*-

__author__ = 'yuer'
from Tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import gui2

root = Tk()
root.geometry('600x400')
root.title('yuer search')
root.iconbitmap('./yuer_logo.ico')


def hello():
    print('hello')


def about():
    label['text'] = "开发者感谢名单\nyuer Creater\n"

menubar = Menu(root)

# 创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# 创建另一个下拉菜单Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)
# 创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# 显示菜单
root.config(menu=menubar)


def on_click_first():
    global page
    page = 1
    f = open(r'./bookcomment.txt', 'r')
    line = f.readline()
    tet = 'page ' + str(page) + ' research:\n'
    j = 0
    while line and j < 5:
        # print line,
        tet = tet + line
        line = f.readline()
        j = j + 1

    line = f.readline()
    while line != '\n' and line:
        tet = tet + line
        line = f.readline()

    f.close()
    # print tet
    label['text'] = tet


def on_click_next():
    global page
    sum = 5 * page
    page = page + 1
    i = 0
    f = open(r'./bookcomment.txt', 'r')
    while i < sum:
        line = f.readline()
        i = i + 1
    line = f.readline()
    if line == '\n':
        line = f.readline()
    tet = 'page ' + str(page) + ' research:\n'
    j = 0
    while line and j < 5:
        # print line,
        tet = tet + line
        line = f.readline()
        j = j + 1
    line = f.readline()
    while line != '\n' and line:
        tet = tet + line
        line = f.readline()

    f.close()
    # print tet
    if not line:
        page = page - 1
        tkinter.messagebox.showinfo(title='提示', message='已经是最后一页了！')
    label['text'] = tet


def on_click_bef():
    global page
    if page > 2:
        sum = 5 * (page - 2)
    else:
        sum = 0
    if page > 1:
        page = page - 1
    else:
        page = 1
        tkinter.messagebox.showinfo(title='提示', message='已经是第一页了！')
    i = 0
    f = open(r'./bookcomment.txt', 'r')
    while i < sum:
        line = f.readline()
        i = i + 1
    line = f.readline()
    if line == '\n':
        line = f.readline()
    tet = 'page ' + str(page) + ' research:\n'
    j = 0
    while line and j < 5:
        # print line,
        tet = tet + line
        line = f.readline()
        j = j + 1
    line = f.readline()
    while line != '\n' and line:
        tet = tet + line
        line = f.readline()

    f.close()
    # print tet

    label['text'] = tet


def on_click_clean():
    global page
    page = 0;
    label['text'] = ''


def on_click_search():
    word = text.get()
    print(text.get())

    from booklist import search
    try:
        f = open('./booklist.txt', 'r')
        topic = f.readline().strip('\n')
        f.close()
        if topic != word:
            search(word)
    except BaseException, e:
        print(e)
    else:
        print ('searching succeed')
        # tkinter.messagebox.showinfo(title='提示', message='搜索成功！')
        gui2.lisgui()


page = 0
text = StringVar()
text.set('Search to what?')
entry = Entry(root)
entry['textvariable'] = text
entry.pack()
buttons = Button(root)
buttons['text'] = '搜索'
buttons['command'] = on_click_search
buttons.pack()

label = Label(root, width=70, height=15, wraplength=600, justify='left', anchor='w')
label.pack()
button = Button(root)
button['text'] = '第一页'
button['command'] = on_click_first
button.pack(side=LEFT)
buttonb = Button(root)
buttonb['text'] = '上一页'
buttonb['command'] = on_click_bef
buttonb.pack(side=LEFT)
buttonn = Button(root)
buttonn['text'] = '下一页'
buttonn['command'] = on_click_next
buttonn.pack(side=LEFT)
clean = Button(root)
clean['text'] = '清空'
clean['command'] = on_click_clean
clean.pack(side=LEFT)

root.mainloop()
