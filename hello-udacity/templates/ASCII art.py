import os
import webapp2
import jinja2
import re
import string
template_dir= os.path.join('C:\Users\Shrinivasan\Desktop\hello-udacity','templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
            t=jinja_env.get_template(template)
            return t.render(params)
    def render(self, template,**kw):
            return self.write(self.render_str(template,**kw))
    def redirect(self, uri, permanent=False, abort=False, code=None,
                 body=None):
        return self.write(self.render_str("success.html"))

class MainPageHandler(MainHandler):


    def get(self):
            self.render("ASCII art.html")

    def post(self):

app = webapp2.WSGIApplication([
('/', MainPageHandler),
    ], debug=True)