#!/usr/bin/env python

import jinja2
import logging
import os
import webapp2

class Email(object):
  def __init__(self, subject, unread, spam=False):
    self.subject = subject
    self.unread = unread
    self.spam = spam
    self.checkSpam()
    msg = "{subject: %s, unread: %s, spam: %s}" % (self.subject, self.unread, self.spam)
    logging.info(msg)

  def checkSpam(self):
    spam_keywords = ['help', 'money', 'account']
    if self.spam == False:
      spam_score = 0
      for word in spam_keywords:
        if word in self.subject:
          spam_score += 1
      if spam_score > 1:
        self.spam = True


class MainHandler(webapp2.RequestHandler):
  emails = [
    Email('First Message', True),
    Email('Second Message', False),
    Email('Help! Send me money from your account.', True),
  ]

  def get(self):
    logging.info("%s.get()" % self.__class__.__name__)
    template = jinja_env.get_template('main.html')
    variables = {
      'name': self.request.get('name'),
      'emails': self.emails,
    }
    self.response.write(template.render(variables))


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

routes = [
  ('/', MainHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
