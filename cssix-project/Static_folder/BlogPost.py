from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    subject = ndb.StringProperty()
    postInformation = ndb.StringProperty()
