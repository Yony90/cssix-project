from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    language = ndb.StringProperty(required=True)
    subject = ndb.StringProperty(required=True)
    text = ndb.StringProperty(required=True)
