import os
import uuid

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import channel

from gdata.alt import appengine
from gdata.photos import service

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'photo.html')

        client_id = str(uuid.uuid4())
        token = channel.create_channel(client_id)

        #client setup
        gd_client = service.PhotosService()
        appengine.run_on_appengine(gd_client)
        #Get picasa album
        albums = gd_client.GetUserFeed(user='sirihikareue0214')
        for album in albums.entry:
            if album.title.text == 'BHTrHunt_sirihikareue0214':
                break
        #Get photo
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (
            'sirihikareue0214',album.gphoto_id.text))
        template_values = {'album': album,'photos': photos,'token' : token,'client_id' : client_id}
        #template_values = {}
        
        self.response.out.write(template.render(path,template_values))

    def post(self):
        client_id = str(self.request.get('client_id'))
        channel.send_message(client_id, 'audio play')

application = webapp.WSGIApplication(
                                    [('/photo',MainPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
                                    
