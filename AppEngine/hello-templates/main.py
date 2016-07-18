#!/usr/bin/env python

import jinja2
import logging
import os
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("%s.get()" % self.__class__.__name__)
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render())


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_loader=jinja2.FileSystemLoader(template_dir)
jinja_environment = jinja2.Environment(loader=jinja_loader)

routes = [
  ('/', MainHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
