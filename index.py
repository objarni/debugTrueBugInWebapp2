import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    raise Exception('This should show in browser!')
    self.redirect('http://www.google.com')


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

