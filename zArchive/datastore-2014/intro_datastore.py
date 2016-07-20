from google.appengine.ext import ndb

class Student(ndb.Model):
  name = ndb.StringProperty(required=True)
  university = ndb.StringProperty(required=True)
  birthday = ndb.DateProperty(required=False)

