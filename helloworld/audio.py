import os

import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'audio.html')

        template_values = {}
        
        self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication(
                                    [('/audio',MainPage)],
                                    debug=True)
