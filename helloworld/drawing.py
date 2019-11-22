#!-*- coding:utf-8 -*-
import os
import time

from google.appengine.api import channel
from google.appengine.ext import webapp2
from google.appengine.ext.webapp2.util import run_wsgi_app
from google.appengine.ext.webapp2 import template
from django.utils import simplejson

class MainPage(webapp2.RequestHandler):
	def get(self):
		# 表示するHTMLファイルのパス取得
		path = os.path.join(os.path.dirname(__file__),'drawing.html')

		# リクエストからtoken(ボード名称)取得
		boardname = self.request.get('bname')

		# ユーザID生成
		user = time.time()

		# Channel生成(リクエストにボード名称がない場合、tokenには固定値"draw"を設定)
		if (boardname):
			token = channel.create_channel(boardname)
		else:
			token = channel.create_channel('draw')
			boardname = 'draw'

		# response生成
		res_values = {
						'token': token,
						'bname':boardname,
					  	'user': user,
						'startx': [],
						'starty': [],
						'endx': [],
						'endy': []
					  }

		self.response.out.write(template.render(path,res_values))

class PostPage(webapp2.RequestHandler):
	def post(self):
		# request取得を連想配列で取得
		req_data = simplejson.loads(self.request.body)

		# Channelで他のユーザに通知
		#channel.send_message('draw',simplejson.dumps(req_data))
		channel.send_message(req_data["bname"],self.request.body)

application = webapp2.WSGIApplication(
									[('/drawing',MainPage),
									('/drawingPost',PostPage)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
