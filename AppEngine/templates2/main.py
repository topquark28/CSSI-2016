#!/usr/bin/env python

import jinja2
import logging
import os
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("%s.get()" % self.__class__.__name__)
        template = jinja_environment.get_template('hello.html')
        self.response.write(template.render())


class GoodByeHandler(webapp2.RequestHandler):
   def get(self):
      logging.info("%s.get()" % self.__class__.__name__)
      self.response.write("Bye!")
     

my_dir = os.path.dirname(__file__)
template_dir = os.path.join(my_dir, 'templates')

jinja_loader=jinja2.FileSystemLoader(template_dir)
jinja_environment = jinja2.Environment(loader=jinja_loader)

routes = [
  ('/', MainHandler),
  ('/bye', GoodByeHandler),
]
app = webapp2.WSGIApplication(routes, debug=True)
