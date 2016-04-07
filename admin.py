import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs
from datetime import datetime

def error_check(self, message):
    fail = False
  
    #Check for required fields
    if self.request.get('student-name') == None or self.request.get('student-name') == '':
        fail = True
        message['name']= 'Student Name must not be blank'
    if self.request.get('college') == None or self.request.get('college') == '':
        fail = True
        message['college']= 'College name must not be blank'
    if self.request.get('email') == None or self.request.get('email') == '':
        fail = True
        message['email']= 'Email must not be blank'
    if self.request.get('ranking') == None or self.request.get('ranking') == '':
        fail = True
        message['ranking']= 'Ranking level must not be blank'

    #Check that you are not creating a duplicate album by editing the name
    for x in db_defs.student.query(ancestor=ndb.Key(db_defs.student, 'student')).fetch():
        if x.name == self.request.get('student-name') and x.key.urlsafe() != self.request.get('student-key'):
            fail = True
            message['duplicate'] = 'A registered student exists with that name'
        
    if fail:
        return 1
    else:
        return 0
    
def pop_student(self, student, message):
    #Perform error validation before populating
    errors = error_check(self, message)

    if errors:
        return 1

    else: 
        #Set student information
        student.name = self.request.get('student-name')
        student.college = self.request.get('college')
        student.email = self.request.get('email')
        student.ranking = self.request.get('ranking')
        student.credits = int(self.request.get('credits-num'))
        student.graduated = self.request.get('graduated-yes')
        
        student.put()
        return 0

#Admin class for get and post handling
class Admin(base_page.BaseHandler):
    
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}

    def get(self):
        self.render('admin.html', self.template_values)
  
    def post(self):
        message = {}
        #Create parent student Key
        studentKey = ndb.Key(db_defs.student, 'student')
        student = db_defs.student(parent=studentKey)

        if pop_student(self, student, message):
            message['0'] = 'Student not saved'
        else:
            message['0'] = 'Student ' + student.name + ' added to the Database!'

        self.template_values['message'] = message
        self.render('admin.html', self.template_values)