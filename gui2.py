# messagebox
# -*- encoding=UTF-8 -*-

from Tkinter import *
import tkinter as tk
from tkinter import messagebox

def lisgui():
    from bookcomment import comment
    class ul:
        url1 = ''
        url2 = ''
        url3 = ''
        url4 = ''
        url5 = ''

    def on_click_first():
        global page
        page = 1
        f = open(r'./booklist.txt', 'r')
        line = f.readline()
        tet = 'page ' + str(page) + ' research:\n'
        label['text'] = '搜索完毕，请选择搜索结果查看短评\n' + tet
        j = 1
        u.url1 = ''
        u.url2 = ''
        u.url3 = ''
        u.url4 = ''
        u.url5 = ''
        while line and j <= 10:
            line = f.readline().strip('\n')
            if j == 1:
                print(line)
                a1['text'] = line
            if j == 3:
                print(line)
                a2['text'] = line
            if j == 5:
                print(line)
                a3['text'] = line
            if j == 7:
                print(line)
                a4['text'] = line
            if j == 9:
                print(line)
                a5['text'] = line
            if j == 2:
                print(line)
                u.url1 = line
                print(u.url1)
            if j == 4:
                print(line)
                u.url2 = line
            if j == 6:
                print(line)
                u.url3 = line
            if j == 8:
                print(line)
                u.url4 = line
            if j == 10:
                print(line)
                u.url5 = line
            j = j + 1
        f.close()

    def on_click_next():
        global page
        sum = 10 * page
        page = page + 1
        i = 0
        f = open(r'./booklist.txt', 'r')
        line = f.readline()
        while i < sum:
            line = f.readline()
            i = i + 1

        tet = 'page ' + str(page) + ' research:\n'
        label['text'] = '搜索完毕，请选择搜索结果查看短评\n' + tet
        j = 1
        u.url1 = ''
        u.url2 = ''
        u.url3 = ''
        u.url4 = ''
        u.url5 = ''
        while line and j <= 10:
            line = f.readline().strip('\n')
            if j == 1:
                print(line)
                a1['text'] = line
            if j == 3:
                print(line)
                a2['text'] = line
            if j == 5:
                print(line)
                a3['text'] = line
            if j == 7:
                print(line)
                a4['text'] = line
            if j == 9:
                print(line)
                a5['text'] = line
            if j == 2:
                print(line)
                u.url1 = line
                print(u.url1)
            if j == 4:
                print(line)
                u.url2 = line
            if j == 6:
                print(line)
                u.url3 = line
            if j == 8:
                print(line)
                u.url4 = line
            if j == 10:
                print(line)
                u.url5 = line
            j = j + 1
        f.close()
        # print tet
        if not line:
            page = page - 1
            tk.messagebox.showinfo(title='提示', message='已经是最后一页了！')

    def on_click_bef():
        global page
        if page > 2:
            sum = 10 * (page - 2)
        else:
            sum = 0
        if page > 1:
            page = page - 1
        else:
            page = 1
            tk.messagebox.showinfo(title='提示', message='已经是第一页了！')
        i = 0
        f = open(r'./booklist.txt', 'r')
        line = f.readline()
        while i < sum:
            line = f.readline()
            i = i + 1
        tet = 'page ' + str(page) + ' research:\n'
        label['text'] = '搜索完毕，请选择搜索结果查看短评\n' + tet
        j = 1
        u.url1 = ''
        u.url2 = ''
        u.url3 = ''
        u.url4 = ''
        u.url5 = ''
        while line and j <= 10:
            line = f.readline().strip('\n')
            if j == 1:
                print(line)
                a1['text'] = line
            if j == 3:
                print(line)
                a2['text'] = line
            if j == 5:
                print(line)
                a3['text'] = line
            if j == 7:
                print(line)
                a4['text'] = line
            if j == 9:
                print(line)
                a5['text'] = line
            if j == 2:
                print(line)
                u.url1 = line
                print(u.url1)
            if j == 4:
                print(line)
                u.url2 = line
            if j == 6:
                print(line)
                u.url3 = line
            if j == 8:
                print(line)
                u.url4 = line
            if j == 10:
                print(line)
                u.url5 = line
            j = j + 1
        f.close()

    page = 0
    u = ul
    window = tk.Tk()
    window.geometry('500x300')
    window.title('yuer select book\'s topic')
    window.iconbitmap('./yuer_logo.ico')
    label = tk.Label(window, text='搜索完毕，请选择搜索结果查看短评\n')
    label.pack()

    def hit1():
        trueurl = u.url1 + 'comments/'
        comment(trueurl)
        tk.messagebox.showinfo(title='提示', message='载入完毕')
        window.destroy()

    def hit2():
        trueurl = u.url2 + 'comments/'
        comment(trueurl)
        tk.messagebox.showinfo(title='提示', message='载入完毕')
        window.destroy()

    def hit3():
        trueurl = u.url3 + 'comments/'
        comment(trueurl)
        tk.messagebox.showinfo(title='提示', message='载入完毕')
        window.destroy()

    def hit4():
        trueurl = u.url4 + 'comments/'
        comment(trueurl)
        tk.messagebox.showinfo(title='提示', message='载入完毕')
        window.destroy()

    def hit5():
        trueurl = u.url5 + 'comments/'
        comment(trueurl)
        tk.messagebox.showinfo(title='提示', message='载入完毕')
        window.destroy()

    a1 = Button(window, text='      ', command=hit1)
    a1.pack()
    a2 = Button(window, text='      ', command=hit2)
    a2.pack()
    a3 = Button(window, text='      ', command=hit3)
    a3.pack()
    a4 = Button(window, text='      ', command=hit4)
    a4.pack()
    a5 = Button(window, text='      ', command=hit5)
    a5.pack()
    button = Button(window)
    button['text'] = '第一页'
    button['command'] = on_click_first
    button.pack(side=LEFT)
    buttonb = Button(window)
    buttonb['text'] = '上一页'
    buttonb['command'] = on_click_bef
    buttonb.pack(side=LEFT)
    buttonn = Button(window)
    buttonn['text'] = '下一页'
    buttonn['command'] = on_click_next
    buttonn.pack(side=LEFT)
    on_click_first()
    window.mainloop()


if __name__ == "__main__":
    lisgui()