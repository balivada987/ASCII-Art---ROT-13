import os
import webapp2
import jinja2
import string
import db
import hashlib
import hmac
import  sqlite3
''''''
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
class MainPageHandler(MainHandler):
    def get(self):
        textinput=self.request.get("textinput")
        p=textinput.encode('rot13')

        self.render("Rot13.html",textinput=p)




app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)
