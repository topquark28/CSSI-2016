from intro_datastore import Student

import jinja2
import logging
import os
import webapp2


class HomeHandler(webapp2.RequestHandler):
  def get(self):
    handlers = []
    for r in routes:
      handler_info = {'path': r[0], 'handler': r[1].__name__ }
      handlers.append(handler_info)
    template_values = {'handlers': handlers}
    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))


class CreateHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('create.html')
    self.response.out.write(template.render(template_values))


class NewStudentHandler(webapp2.RequestHandler): 
  def get(self):
    name = self.request.get('name')
    university = self.request.get('university')

    student = Student(name=name, university=university)
    student.put()

    template_values = {
      'name': name,
      'university': university,
    }
    template = jinja_environment.get_template('create.html')
    self.response.out.write(template.render(template_values))


class QueryHandler(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('name')
    my_query = Student.query()
    students = my_query.fetch()
    template_values = { 'students': students }
    template = jinja_environment.get_template('queryresults.html')
    self.response.out.write(template.render(template_values))


class FilteredQueryHandler(webapp2.RequestHandler):
  def get(self):
    filter_str = self.request.get('filter')
    if not filter_str:
      filtered_query = Student.query()
    else:
      filtered_query = Student.query().filter(eval(filter_str))
    students = filtered_query.fetch()
    logging.info('Filter string: ' + filter_str)
    logging.info(students)
    template_values = { 'students': students, 'filter_str': filter_str }
    template = jinja_environment.get_template('queryresults.html')
    self.response.out.write(template.render(template_values))


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

routes = [
    ('/', HomeHandler),
    ('/create', CreateHandler),
    ('/newstudent', NewStudentHandler),
    ('/filteredquery', FilteredQueryHandler),
    ('/query', QueryHandler),
  ]

app = webapp2.WSGIApplication(routes, debug=True)

