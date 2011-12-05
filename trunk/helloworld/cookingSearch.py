import urllib2
import time
from BeautifulSoup import BeautifulSoup
from htmlentity2unicode import htmlentity2unicode as html2uni

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from django.utils import simplejson

class RPCHandler(webapp.RequestHandler):
    def get(self):
        # ���N�G�X�g�p�����[�^�擾
        query = simplejson.loads(self.request.get('query'))
        monRange = simplejson.loads(self.request.get('monRange'))
        # ���ݓ����擾
        today = time.localtime()
        # ���ݓ�������N�����擾
        # URL�Ɏ擾�����N���𖄂ߍ���
        urltext = 'http://wifeshomecooking.blogspot.com/%04d_%02d_01_archive.html' % (today.tm_year,today.tm_mon)
        # ���ʃ��X�g
        results = []
        _cookingSearch(urltext,query,results)

        # ���N�G�X�g�p�����[�^'monRange'�͈̔͂�query����
        for i in range(int(monRange)):
            year = today.tm_year
            mon = today.tm_mon - (i+1)
            if mon <= 0:
                year -= 1
                mon += 12
            urltext = 'http://wifeshomecooking.blogspot.com/%04d_%02d_01_archive.html' % (year,mon)
            _cookingSearch(urltext,query,results)

        self.response.out.write(simplejson.dumps(results))

    def _cookingSearch(purltext,pquery,presults):
        # URL�ɐڑ����Ahtml���擾
        openurl = urllib2.urlopen(purltext)
        html = openurl.read()
        # BeautifulSoup��div�^�O�̗v�f���擾
        soup = BeautifulSoup(html)
        divlist = soup.findAll('div')
        # �K�v��div�^�O�̓��e�݂̂𒊏o
        divlist2 = []
        for div in divlist:
            try:
                if div['class'] == 'post-body entry-content':
                            divlist2.append(div)
            except KeyError:
                print 'KeyError_div class post-body entry-content'
        # h3�^�O�̗v�f���擾
        h3s = soup.findAll('h3')
        # �K�v��div�^�O�̓��e�݂̂𒊏o
        h3s2 = []
        for h3 in h3s:
            try:
                if h3['class'] == 'post-title entry-title':
                    h3s2.append(h3)
            except KeyError:
                print 'KeyError_h3 class post-title entry-title'

        # query�Ƀ}�b�`������̂����ʂɒǉ�
        for i in range(len(divs2)):
            text = html2uni(divs2[i].getText())
            title = print h3s2[i].findAll('a')[0].text
            url = h3s2[i].findAll('a')[0]['href']

            if text.find(pquery) >= 0:
                result = {'text':text,'title':title,'url':url}
                presults.append(result)

application = webapp.WSGIApplication(
                                    [('/cookingSearch',RPCHandler)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
