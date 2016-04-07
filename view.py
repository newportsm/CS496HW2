import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs
from datetime import datetime

class View(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
  
    def get_values(self):
        self.template_values['student'] = [{
        'name':x.name, 
        'college':x.college, 
        'email':x.email, 
        #'birthday':x.birthday,
        'ranking':x.ranking,
        'credits':x.credits,
        'graduted':x.graduated,
        'key':x.key.urlsafe()} for x in db_defs.student.query(ancestor=ndb.Key(db_defs.student, 'student')).fetch()]
    
    def get(self):
        self.get_values()
        self.render('view.html', self.template_values)
  
