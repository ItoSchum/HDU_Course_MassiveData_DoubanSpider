# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


def lis(word):
    furl = 'https://book.douban.com/tag/'
    url = furl + word
    print(url)
    return url


def search(word):
    url = lis(word)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    }
    f = open('./booklist.txt', 'wb')
    f.write(word + '\n')
    f.close()
    i = 0
    while i < 30:
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'lxml')

        booknames = soup.select('li.subject-item > div.info > h2 > a')
        pn = soup.select('span.next > a')
        try:
            # print(pn[0].get('href'))
            url = 'https://book.douban.com' + pn[0].get('href')
        except IndexError, e:
            print(e)
            print ('已经到底了')
            break
        f = open('./booklist.txt', 'a')
        for index, item in enumerate(booknames):
            print item.get('title').strip().strip('\n') + ' : ' + item.get('href') + '\n'
            f.write(item.get('title').strip().strip('\n') + '\n' + item.get('href').strip().replace('\n', ' ') + '\n')
        f.close()
        i = i + 1


if __name__ == "__main__":
    # print("main")
    word = raw_input()
    search(word)
    # url = 'https://book.douban.com/subject/1148282/comments/'
    # bookcomment.comment(url)
