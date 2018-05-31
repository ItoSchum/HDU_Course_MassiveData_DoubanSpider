
# -*- coding: utf-8 -*-
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def lis(word):
    furl = 'https://book.douban.com/subject_search?search_text='
    burl = '&cat=1001'
    url = furl + word + burl
    print(url)
    return url


def search(word):
    url = 'https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
    }

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')

    booknames = soup.select('li.subject-item > div.info > h2 > a')
    for index, item in enumerate(booknames):
        print item.get('title').strip().strip('\n') + '\n'



if __name__ == "__main__":
    print("main")
    search('https://book.douban.com/tag/%E5%8E%86%E5%8F%B2')
    # url = 'https://book.douban.com/subject/1148282/comments/'
    # bookcomment.comment(url)

