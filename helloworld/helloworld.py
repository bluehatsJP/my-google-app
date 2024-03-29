import cgi
import os

from google.appengine.api import users
import webapp2
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            }

        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))
"""
    def get(self):
        self.response.out.write('<html><body>')

        greetings = db.GqlQuery("SELECT * FROM Greeting ORDER BY date DESC LIMIT 10")

        for greeting in greetings:
            if greeting.author:
                self.response.out.write('An anonymous person wrote:')
            else:
                self.response.out.write('<blockquote>%s</blockquote>' %
                                        cgi.escape(greeting.content))
"""
        #self.response.out.write("""
        #    <form action="/sign" method="post">
        #        <div><textarea name="content" row="3" cols="60"></textarea></div>
        #        <div><input type="submit" value="Sign Guestbook"></div>
        #    </form>
        #    </body></html>""")

class Guestbook(webapp2.RequestHandler):
    def post(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')

app = webapp2.WSGIApplication(
                                    [('/',MainPage),
                                     ('/sign',Guestbook)],
                                    debug=True)                                    
