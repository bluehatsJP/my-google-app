import os

from google.appengine.ext import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'audio.html')

        template_values = {}
        
        self.response.out.write(template.render(path,template_values))

application = webapp2.WSGIApplication(
                                    [('/audio',MainPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
                                    
