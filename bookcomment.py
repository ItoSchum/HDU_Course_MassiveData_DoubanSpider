# coding:utf-8
# 爬取豆瓣图书短评
import sys
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def comment(giveurl):
    url = giveurl
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    }
    i = 0
    while i < 31:
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'lxml')
        # users:用户列表    comments:评论列表
        bookname=soup.select('#content > h1')
        count = soup.select('#total-comments')
        users = soup.select('div.comment > h3 > span.comment-info > a')
        comments = soup.select('li.comment-item > div.comment > p')
        pnext = soup.select('ul.comment-paginator > li.p > a')
        # print pnext[0].get_text()
        # print onclick
        # print count[0].get_text().split('全部共')[1].split('条')[0]
        # print comments[4].get_text().strip().replace('\n',' ')
        if i == 0:
            onclick = pnext[0].get('href')
            #print onclick
            url = giveurl + onclick
            f = open('./bookcomment.txt', 'wb')
            print bookname[0].get_text()+'\n'
            print count[0].get_text()+ '\n'
            f.write(bookname[0].get_text() + '\n')
            f.write(count[0].get_text() + '\n')
        else:
            try:
                onclick = pnext[2].get('href')
            except IndexError,e:
                print ('已经到底了')
                print e
                break
            url = giveurl + onclick
            f = open('./bookcomment.txt', 'a')
        # f.write(count[0].get_text()+'\n')
        for index, item in enumerate(comments):
            print users[index].get_text() + ':' + item.get_text().strip().strip('\n') + '\n'
            f.write(users[index].get_text() + ':' + item.get_text().strip().replace('\n', ' ') + '\n\n')
        f.close()
        i = i + 1


if __name__ == "__main__":
    #print("main")
    url = 'https://book.douban.com/subject/6709783/comments/'
    comment(url)
