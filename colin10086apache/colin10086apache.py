from app.form import Form

class colin10086apache(Form):

 def validate(_self, form_data):
  valid = True
  if ‘ghost’ not in form_data or \
   ‘docroot’ not in form_data or \
   ‘hostname’ not in form_data or \
   ‘source_repo’ not in form_data:
   valid = False
  if valid is False:
   return “Missing info!”
  return True

 def process(_self, form_data):
  nodes = {}
  hostname = form_data[‘hostname’]
  ghost = form_data[‘vhost’]
  nodes[hostname] = {}
  nodes[hostname][‘classes’] = [‘colin10086_apache’]
  nodes[hostname][‘colin10086_apache::vhost’] = vhost
  nodes[hostname][‘colin10086_apache::docket’] = form_data[‘docroot’]
  nodes[hostname][‘colin10086_apache::source_repo’] = form_data[‘source_repo’]

  return nodes

