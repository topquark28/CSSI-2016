#!/usr/bin/env python

import jinja2
import logging
import os
import webapp2

class MainHandler(webapp2.RequestHandler):

    def get(self):
      logging.info("%s.get()" % self.__class__.__name__)
      template = jinja_environment.get_template('main.html')
      self.response.out.write(template.render())

    def post(self):
      logging.info("%s.get()" % self.__class__.__name__)
      self.response.out.write("You have submitted your madlib")
      template = jinja_environment.get_template('results.html')
      variables = {
        'noun1': self.request.get("noun1"),
        'activity': self.request.get("activity"),
        'teacher': self.request.get("teacher"),
        'celebrity': self.request.get("celebrity"),
        'show': self.request.get("show"),
        'fun': self.request.get("fun"),
      }
      self.response.out.write(template.render(variables))


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_loader=jinja2.FileSystemLoader(template_dir)
jinja_environment = jinja2.Environment(loader=jinja_loader)

routes = [
  ('/', MainHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
