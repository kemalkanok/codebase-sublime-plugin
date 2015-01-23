import sublime,sublime_plugin,urllib2,json,urllib,uuid

class SendcodeCommand(sublime_plugin.TextCommand):
	
	
		
		
	def run(self, edit):
		self.auth = []
		self.data = ""
		sels = self.view.sel();
		data= self.view.substr(sels[0])
		if  len(data) <= 3:
			print "alert!"
		else:
			self.data = data
			if self.loginCheck() == 0:
				self.view.window().show_input_panel("Email:","",self.ondone,None,None)
				print "login or register"
	def ondone(self,value):
		self.auth.append(value)
		self.view.window().show_input_panel("Password:","",self.ondone2,None,None)
	def ondone2(self,value):
		self.auth.append(value)
		print self.auth
		sublime.status_message("Trying to login...");
		if self.login() == 1:
			self.view.window().show_input_panel("send To Codebase?:",self.data,self.ondone3,None,None)
	def ondone3(self,value):
		url = 'http://77.81.243.69/post'
		params = urllib.urlencode({
		  'title' : uuid.uuid1(),
		  'content': value,
		  'language_id': 1
		})
		response = urllib2.urlopen(url, params).read()
		response = json.loads(response)
		print response
		if response["status"] == 403:
			sublime.status_message("Sent Operation Failed!")
			return 0
		else:
			sublime.status_message("Sent Operation Complete")
			return 1
		pass
		pass
	def login(self):
		url = 'http://77.81.243.69/auth'
		params = urllib.urlencode({
		  'email': self.auth[0],
		  'password': self.auth[1]
		})
		response = urllib2.urlopen(url, params).read()
		response = json.loads(response)
		if response["status"] == 403:
			sublime.status_message("login fail try again")
			return 0
		else:
			sublime.status_message("login complete")
			return 1
		pass
	def loginCheck(self):
		url = 'http://77.81.243.69/auth'
		response = urllib2.urlopen(url).read()
		response = json.loads(response)
		if response["status"] == 403:
			return 0
		else:
			return 1 

		#self.view.insert(edit, 0, "Hello, World!")
class ReadcodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
