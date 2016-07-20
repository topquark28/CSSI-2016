import cssi_data
import jinja2
import logging
import os
import webapp2


class Student(object):
  def __init__(self, name, full_name):
    self.name = name
    self.full_name = full_name
    self.photo = 'static/' + cssi_data.PHOTOS[name]
    self.school = cssi_data.SCHOOLS[name]


students = []
def load_students_list():
  for name in cssi_data.STUDENTS:
    student = Student(name, cssi_data.FULL_NAMES[name])
    students.append(student)

def find_student_by_name(name):
  result = None
  for student in students:
    if student.name == name:
      result = student
      break
  return result


class HomeHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {'students': students}
    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))


class ProfileHandler(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('name')

    if name in cssi_data.STUDENTS:
      student = find_student_by_name(name)
      template_values = student.__dict__
      template_file = 'profile.html'
    else:
      self.error(404)
      template_file = 'profile_error.html'

    logging.info(template_values)

    template = jinja_environment.get_template(template_file)
    self.response.out.write(template.render(template_values))


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

my_handlers = [
    ('/', HomeHandler),
    ('/profile.*', ProfileHandler)
  ]

load_students_list()
app = webapp2.WSGIApplication(my_handlers, debug=True)

