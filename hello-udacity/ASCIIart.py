import wsgiref.handlers
import db
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
    def redirect(self, template,**kwargs):
        return self.write(self.render_str(template))
class Art(db.Model):
    Title=db.StringProperty(required=True)
    Image=db.TextProperty(required=True)
    Created=db.DateTimeProperty(auto_now_add=True)

class MainPageHandler(MainHandler):
    def render_front(self,Title="",Image="",error=""):
        self.render("ASCII art.html",Title=Title,Image=Image,error=error)

    def get(self):

        self.render("ASCII art.html")


    def post(self):
        Image = self.request.get("Image")
        Title=self.request.get("Title")
        error="Hi How are you"
        if Image and Title:
            a=Art(Title=Title,Image=Image)
            a.put()
            self.redirect("ASCII art.html")


        else:self.render_front(error=error)


app = webapp2.WSGIApplication([('/', MainPageHandler),
    ], debug=True)