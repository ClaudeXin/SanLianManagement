from entitybook import BasicBook
from entitybook import BookSearchByName
from entitybook import BookSearchByAuth
from entitybook import BookSearchByCategorical
from entitybook import BookSearchByPublisher
from entitybook import BookSearchByIsbn
from entitybook import BookOrderByHotPoint
from entitybook import BookControlNumber
import re

class BookDetail(object):
	def __init__(self, arg):
		self.insert(arg)

	def insert(self, arg):
		name_match = re.compile(u"\uFF08.*?\uFF09")
		self.book_name = name_match.sub("",arg.book_name).replace("&nbsp;", "")
		self.book_auth_name = arg.book_auth_name
		self.book_isbn = arg.book_isbn
		self.book_publisher = arg.book_publisher
		if args[4] != None:
			self.book_word = arg.book_word
		else:
			self.book_word = ""
		if args[5] != None:
			self.book_publish_time = arg.book_publish_time
		else:
			self.book_publish_time = ""
		if args[6] != None:
			self.book_introduce = arg.book_introduce.replace("&nbsp;", "")
		else:
			self.book_introduce = ""

class HotBookDetail(object):
	def __init__(self, arg):
		self.insert(arg)

	def insert(self, arg):
		name_match = re.compile(u"\uFF08.*?\uFF09")
		self.book_name = name_match.sub("",arg.book_name).replace("&nbsp;", "")
		self.book_isbn = arg.book_isbn
		if args[2] != None:
			self.book_remain = arg.book_remain
		else:
			self.book_remain = 0
		if args[3] != None:
			self.book_hot_point = arg.book_hot_point
		else:
			self.book_hot_point = 0
		
class BookManager(object):
	def __init__(self):
		self.book = BasicBook()

	def search(self, arg):
		temp = []
		temp.extend(BookSearchByName(self.book, arg))
		temp.extend(BookSearchByAuth(self.book, arg))
		temp.extend(BookSearchByCategorical(self.book, arg))
		temp.extend(BookSearchByPublisher(self.book, arg))
		temp.extend(BookSearchByIsbn(self.book, arg))
		result = []
		for element in temp:
			result.append(BookDetail(element))
		return result

	def showhot(self, state, number):
		temp = BookOrderByHotPoint(self.book, state)
		return BookControlNumber(temp, 0, number+1)
