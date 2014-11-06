from django.shortcuts import render



class ShowPage(object):
	def __init__(self):
		self.index_path = "/manager/index.html"
		self.login_path = "/manager/login.html"
		self.addseller_path = "/manager/addseller.html"
		self.dict_path = "/manager/dict.html"
		self.informanager_path = "/manager/informanager.html"
		self.loadok_path = "/manager/loadok.html"
		self.showteam_path = "/manager/showteam.html"

	def showIndex(self, request, salesoption, record, book):
		return render(request, self.index_path, 
			{"salesoption": salesoption, "record": record, "book": book})

	def showLogin(self, request, message):
		return render(request, self.login_path, 
			{"message": message})

	def showTeam(self, request):
		return render(request, self.showteam_path)

	def showDict(self, request):
		return render(request, self.dict_path)

	def showLoadOk(self, request):
		return render(request, self.loadok_path)

	def showInformanager(self, request):
		return render(request, self.informanager_path)

	def showAddseller(self, request, message):
		return render(request, self.addseller_path,
			{"message": message})