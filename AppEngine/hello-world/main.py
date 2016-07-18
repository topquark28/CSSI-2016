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
import logging
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("%s.get()" % self.__class__.__name__)
        self.response.write('Hello, Chris!')


class LogicHandler(webapp2.RequestHandler):
  def get(self):
    logging.info("%s.get()" % self.__class__.__name__)
    if True:
      self.response.write('The truth will set you free.')
    else:
      self.response.write('How did I get here?')

class GoodByeHandler(webapp2.RequestHandler):
  def get(self):
    logging.info("%s.get()" % self.__class__.__name__)
    self.response.write('Goodbye, Dave.')


handlers = [
  ('/', MainHandler),
  ('/bye', GoodByeHandler),
  ('/logic', LogicHandler),
]

app = webapp2.WSGIApplication(handlers, debug=True)
