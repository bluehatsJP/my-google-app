#!-*- coding:utf-8 -*-
import urllib

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class RPCHandler(webapp.RequestHandler):
    def get(self):
		# リクエストパラメータ取得
		lang = self.request.get('tl').encode('utf_8')
		text = self.request.get('q').encode('utf_8')
		#lang = self.request.get('tl').encode('shift_jis')
		#text = self.request.get('q').encode('shift_jis')
		query = urllib.urlencode({'tl':lang,'q':text})
		urltext = 'http://translate.google.com/translate_tts?' + query

		#opener = urllib2.build_opener()
		#opener.addheaders = [('Referer','')]
		#res = opener.open('http://translate.google.com/translate_tts?q=hello')

		#req = urllib2.Request(url='http://translate.google.com/translate_tts?q=hello')
		#req.add_header('Referer','');
		#res = urllib2.urlopen(req)

		res = urlfetch.fetch(url=urltext,
							method=urlfetch.GET,
							headers={'Referer':''})

		if res.status_code == 200:
			self.response.headers["Content-Type"] = "audio/mpeg"
			self.response.out.write(res.content)
			#self.response.out.write(res.headers['content-length'])
		else:
			self.response.out.write('error.status_code == ' + res.status_code)

application = webapp.WSGIApplication(
                                    [('/readingOut',RPCHandler)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
