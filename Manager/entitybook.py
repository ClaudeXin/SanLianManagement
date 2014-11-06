#coding:utf-8
from models import Book

class InterfaceBook(object):
	def getValue(self):
		pass

class BasicBook(InterfaceBook):
	def __init__(self):
		self.result = Book.objects.all()

	def getValue(self):
		return self.result

#book search method
class BookSearchByName(InterfaceBook):
	def __init__(self, book, arg):
		self.result = book.getValue()
		self.__work(arg)

	def __work(self, arg):
		self.result = self.result.filter(book_name__contains=arg)

	def getValue(self):
		return self.result

class BookSearchByAuth(BookSearchByName):
	def __init__(self, book, arg):
		BookSearchByName.__init__(self, book, arg)

	def __work(self, arg):
		self.result = self.result.filter(book_auth_name__contains=arg)

class BookSearchByCategorical(BookSearchByName):
	def __init__(self, book, arg):
		BookSearchByName.__init__(self, book, arg)

	def __work(self, arg):
		self.result = self.result.filter(book_categorical__contains=arg)

class BookSearchByPublisher(BookSearchByName):
	def __init__(self, book, arg):
		BookSearchByName.__init__(self, book, arg)

	def __work(self, arg):
		self.result = self.result.filter(book_publisher__contains=arg)

class BookSearchByIsbn(BookSearchByName):
	def __init__(self, book, arg):
		BookSearchByName.__init__(self, book, arg)

	def __work(self, arg):
		self.result = self.result.filter(book_isbn__contains=arg)

#book order method
class BookOrderByTime(InterfaceBook):
	def __init__(self, book, arg):
		self.result = book.getValue()
		self.__work(arg)

	def __work(self, arg):
		if arg == 0:
			self.result = self.result.order_by('book_publish_time')
		else:
			self.result = self.result.order_by('-book_publish_time')

	def getValue(self):
		return self.result

class BookOrderByHotPoint(BookOrderByTime):
	def __init__(self, book, arg):
		BookOrderByTime.__init__(self, book, arg)

	def __work(self, arg):
		if arg == 0:
			self.result = self.result.order_by('book_hot_point')
		else:
			self.result = self.result.order_by('-book_hot_point')

class BookOrderByPrice(BookOrderByTime):
	def __init__(self, book, arg):
		BookOrderByTime.__init__(self, book, arg)

	def __work(self, arg):
		if arg == 0:
			self.result = self.result.order_by('book_price')
		else:
			self.result = self.result.order_by('-book_price')

#book number
class BookControlNumber(InterfaceBook):
	def __init__(self, book, start, end):
		self.result = book.getValue()
		self.__work(start, end)

	def __work(self, start, end):
		self.result = self.result[start: end]

	def getValue(self):
		return self.result
