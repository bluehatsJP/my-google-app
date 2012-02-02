#!-*- coding:utf-8 -*-
import urllib2

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class RPCHandler(webapp.RequestHandler):
    def get(self):
        # リクエストパラメータ取得
        #lang = self.request.get('lang')
        #text = self.request.get('text')
        #urltext = 'http://translate.google.com/translate_tts?tl=%s&q=%s' % (lang,text)

		opener = urllib2.build_opener()
		opener.addheaders = [('Referer','')]
		res = opener.open('http://translate.google.com/translate_tts?q=hello')

		#self.response.out.write(res)
		doSomethingWithResult(res)

application = webapp.WSGIApplication(
                                    [('/readingOut',RPCHandler)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
