import urllib2
import time
from BeautifulSoup import BeautifulSoup
from htmlentity2unicode import htmlentity2unicode as html2uni


today = time.localtime()
urltext = 'http://wifeshomecooking.blogspot.com/%04d_%02d_01_archive.html' % (today.tm_year,today.tm_mon)
openurl = urllib2.urlopen(urltext)
html = openurl.read()
soup = BeautifulSoup(html)
divlist = soup.findAll('div')
divlist2 = []

for div in divlist:
    try:
        if div['class'] == 'post-body entry-content':
                    divlist2.append(div)
    except KeyError:
        print 'KeyError'

h3s = soup.findAll('h3')
h3s2 = []
for h3 in h3s:
    try:
	if h3['class'] == 'post-title entry-title':
    	    h3s2.append(h3)
	except KeyError:
            print 'KeyError'

text = divs2[0].getText()
title = print h3s2[0].findAll('a')[0].text
url = h3s2[0].findAll('a')[0]['href']
