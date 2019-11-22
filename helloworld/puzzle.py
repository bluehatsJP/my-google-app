import os
import random

from google.appengine.ext import webapp2
from google.appengine.ext.webapp2.util import run_wsgi_app
from google.appengine.ext.webapp2 import template

from gdata.alt import appengine
from gdata.photos import service

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'puzzle.html')

        #client setup
        gd_client = service.PhotosService()
        appengine.run_on_appengine(gd_client)
        #Get picasa album
        albums = gd_client.GetUserFeed(user='sirihikareue0214')
        for album in albums.entry:
            if album.title.text == 'BHTrHunt_sirihikareue0214':
                break
        #Get photos
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (
            'sirihikareue0214',album.gphoto_id.text))
        #Get photo
        i = 0
        randint = random.randrange(len(photos.entry))
        for photo in photos.entry:
            if i == randint:
		        break
            i+=1

        template_values = {'album': album,'photos': photos,'photo': photo}
        
        self.response.out.write(template.render(path,template_values))

application = webapp2.WSGIApplication(
                                    [('/puzzle',MainPage)],
                                    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
                                    
