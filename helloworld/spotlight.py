import os
import random

webapp2
from google.appengine.ext.webapp import template

from gdata.alt import appengine
from gdata.photos import service

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'spotlight.html')

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

app = webapp2.WSGIApplication(
                                    [('/spot',MainPage)],
                                    debug=True)
