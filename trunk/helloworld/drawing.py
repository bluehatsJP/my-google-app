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
		# �\������HTML�t�@�C���̃p�X�擾
		path = os.path.join(os.path.dirname(__file__),'drawing.html')

		# ���N�G�X�g����token(�{�[�h����)�擾
		boardname = self.request.get('bname')

		# ���[�UID����
		user = time.time()

		# Channel����(���N�G�X�g�Ƀ{�[�h���̂��Ȃ��ꍇ�Atoken�ɂ͌Œ�l"draw"��ݒ�)
		if (boardname):
			token = channel.create_channel(boardname)
		else:
			token = channel.create_channel('draw')
			boardname = 'draw'

		# response����
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

class PostPage(webapp.RequestHandler):
	def post(self):
		# request�擾��A�z�z��Ŏ擾
		req_data = simplejson.loads(self.request.body)

		# Channel�ő��̃��[�U�ɒʒm
		#channel.send_message('draw',simplejson.dumps(req_data))
		channel.send_message(req_data["bname"],self.request.body)

application = webapp.WSGIApplication(
									[('/drawing',MainPage),
									('/drawingPost',PostPage)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
