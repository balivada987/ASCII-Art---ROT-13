#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
'''
import webapp2
form ="""
<form method="post">
 <label> Month <input type="text" name="month value="%(month)s"></label>
 <label> Year <input type="text" name="year" value="%(year)s"></label>
 <label> Date <input type="text" name="date" value="%(date)s"></label>
   <input type="submit" name="date">
  <div> <b>%(error)s</b></div>

</form>"""
pon="""<form action="/testform"> <input name="p">
<p>success</p>
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self,errors="",month="",date="",year=""):
        self.response.out.write(form %{"error":errors,"month":month,"date":date,"year":year})
    def get(self):
        self.write_form()

    def post(self):
        user_month=self.request.get('month')
        user_year=self.request.get('year')
        user_day=self.request.get('day')
        month=valid_month(user_month)
        year=valid_year(user_year)
        date=valid_day(user_day)
        if not ( month,year ,day):self.response.write("Hi You are gud",user_month,user_year,user_day)

        else:self.write_form("It is an error")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

n=0
day=0
monthname={"Jan","Feb","March","April","May","June", "July","Aug","Sep","Oct","Nov","Dec"}
def valid_year(year):
        if (year>1985 and year <2005):return year
        else:return n
def valid_month(month):
        if  month in monthname: return month
        else:return n
def valid_day(day):

        if  ( (day > 0 and day <= 31)):return day
        else:return n

////////////////////shoping list
form_html="""
<form>
 <label> Food Name<input type="text" name="food" value="food"> </label>
 <input type="hidden" name="hidden" value="eggs"> food</input>
 <input type="submit" name="add"></input>
 </form>
"""
hidden_html="""
<form>
 <label> Food Name<input type="hidden" name="food" value="%s"> </label>
</form>"""
item_html="""
<list> %s</list>"""
shopping_list_html="""
<form>
<h2>Shopping List</h2>
 <ul>
 %s
 </ul>
</form>
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
        n=self.request.get("n")
        if n:
            n=int(n)
        self.render("form_html.html",animal1=self.request.get("Animal1"),n=n)


'''

import os
import webapp2
import jinja2
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
        items=self.request.get_all("food")


        self.render("Rot13.html",items=items)



    """    def get(self):
        output=form_html
        output_hidden=""
        output_items=""
        form_items=""
        items=self.request.getall('food')
        if items:
            for item in items:
                output_hidden += hidden_html %item
                output_items +=item_html %item

                shopping_list=shopping_list_html %item
                output=shopping_list %

"""
app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)
