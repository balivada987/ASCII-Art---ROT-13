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
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainPageHandler(MainHandler):
    have_error = False
    def get(self):

        self.render("signup.html")


    def post(self):
        have_error=False
        username=self.request.get("username")
        password=self.request.get("password")
        verify=self.request.get("verify")
        email=self.request.get("email")


        params = dict(username=username,email=email)
        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True
        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.redirect('success.html',username)





app = webapp2.WSGIApplication([
('/', MainPageHandler),
    ], debug=True)
