import cgitb
import cgi



class controllerClass:
  def __init__(self):
    self.params=cgi.FieldStorage()
    self.view=''
  
  def parseRequest(self):
    if self.params.getvalue('view')<>None:
      self.view=self.params.getvalue('view')
    else:
       self.view='main'
      
    
  def proceed(self,tl):
    tl.process(self.view+'.tpl')
    
  
  
  def redirect(self):
    pass