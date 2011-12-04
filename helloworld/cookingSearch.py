import urllib2
import time
from BeautifulSoup import BeautifulSoup
from htmlentity2unicode import htmlentity2unicode as html2uni

# 現在日時取得
today = time.localtime()
# 現在日時から年月を取得
# URLに取得した年月を埋め込み
urltext = 'http://wifeshomecooking.blogspot.com/%04d_%02d_01_archive.html' % (today.tm_year,today.tm_mon)
# URLに接続し、htmlを取得
openurl = urllib2.urlopen(urltext)
html = openurl.read()
# BeautifulSoupでdivタグの要素を取得
soup = BeautifulSoup(html)
divlist = soup.findAll('div')
# 必要なdivタグの内容のみを抽出
divlist2 = []
for div in divlist:
    try:
        if div['class'] == 'post-body entry-content':
                    divlist2.append(div)
    except KeyError:
        print 'KeyError_div class post-body entry-content'
# h3タグの要素を取得
h3s = soup.findAll('h3')
# 必要なdivタグの内容のみを抽出
h3s2 = []
for h3 in h3s:
    try:
	if h3['class'] == 'post-title entry-title':
    	    h3s2.append(h3)
    except KeyError:
        print 'KeyError_h3 class post-title entry-title'

text = divs2[0].getText()
title = print h3s2[0].findAll('a')[0].text
url = h3s2[0].findAll('a')[0]['href']
