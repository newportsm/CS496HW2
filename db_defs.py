from google.appengine.ext import ndb

class student(ndb.Model):
    name = ndb.StringProperty(required=True)
    college = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    #ranking is freshman, sophmore, junior, senior
    ranking = ndb.StringProperty(required=True)
    credits = ndb.IntegerProperty()
    graduated = ndb.StringProperty()