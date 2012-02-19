#!-*- coding:utf-8 -*-
import os
import time

from google.appengine.api import channel
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from django.utils import simplejson

class MainPage(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__),'drawing.html')

		# ユーザID生成
		user = time.time()

		# Channel生成
		token = channel.create_channel('draw')

		# response生成
		res_values = {
						'token': token,
					  	'user': user,
						'startx': [],
						'starty': [],
						'endx': [],
						'endy': []
					  }

		self.response.out.write(template.render(path,res_values))

class PostPage(webapp.RequestHandler):
	def post(self):
		# request取得
		#req_data = self.request.get('data')

		# Channelで他のユーザに通知
		#channel.send_message('draw',simplejson.dumps(req_data))
		channel.send_message('draw',self.request.body)

application = webapp.WSGIApplication(
									[('/drawing',MainPage),
									('/drawingPost',PostPage)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
