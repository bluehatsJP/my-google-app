#!-*- coding:utf-8 -*-
import urllib2

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class RPCHandler(webapp.RequestHandler):
    def get(self):
        # リクエストパラメータ取得
        #lang = self.request.get('tl')
        #text = self.request.get('q')
        #urltext = 'http://translate.google.com/translate_tts?tl=%s&q=%s' % (lang,text)

		#opener = urllib2.build_opener()
		#opener.addheaders = [('Referer','')]
		#res = opener.open('http://translate.google.com/translate_tts?q=hello')

		#req = urllib2.Request(url='http://translate.google.com/translate_tts?q=hello')
		#req.add_header('Referer','');
		#res = urllib2.urlopen(req)

		res = urlfetch.fetch(url= 'http://translate.google.com/translate_tts?q=hello',
							method=urlfetch.GET,
							headers={'Referer':''})

		self.response.headers["Content-Type"] = "audio/mpeg"
		self.response.out.write(res.content)
		#doSomethingWithResult(res)

application = webapp.WSGIApplication(
                                    [('/readingOut',RPCHandler)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
