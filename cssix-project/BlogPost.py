from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    subject = ndb.StringProperty(required=True)
    text = ndb.StringProperty(required=True)
