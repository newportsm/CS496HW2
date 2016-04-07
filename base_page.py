import webapp2
import os
import jinja2

class BaseHandler(webapp2.RequestHandler):
  
  #Used the cached property to not have to re-calc each time
  @webapp2.cached_property
  def jinja2(self):
    return jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )
  
  def render(self, template, template_variables={}):
    template = self.jinja2.get_template(template)
    self.response.write(template.render(template_variables))