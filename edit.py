import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs
from datetime import datetime
import admin

class Edit(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
  
    def get(self):
        
        student_key = ndb.Key(urlsafe=self.request.get('key'))
        student = student_key.get()
        student.urlsafe = self.request.get('key')
        self.template_values['student'] = student
        self.render('admin.html', self.template_values)
        #except:
            #self.redirect('/view')
      
    def post(self):
        message = {}
        student_key = ndb.Key(urlsafe=self.request.get('student-key'))
        student = student_key.get()
    
    #Set student information
        if admin.pop_student(self, student, message):
            message['0'] = 'Student not updated'
            student.urlsafe = student_key.urlsafe()
            self.template_values['student'] = student
            self.template_values['message'] = message
            self.render('admin.html', self.template_values)
        #else:
            #Render the changes with a confirmation message
            #self.redirect('/view')

  