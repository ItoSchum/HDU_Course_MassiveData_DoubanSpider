
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def list(word):
    furl = 'https://book.douban.com/subject_search?search_text='
    burl = '&cat=1001'
    url = furl + word + burl
    print(url)
    return url


if __name__ == "__main__":
    # print("main")
    # url = 'https://book.douban.com/subject/1148282/comments/'
    # bookcomment.comment(url)
    url = list('计算机')
