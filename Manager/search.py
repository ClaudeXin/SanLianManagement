#-*-coding:utf-8-*-
from models import Book,RecordWeb
import datetime

#search interface 
class Search():
    def search(self):
        pass
    def getValue(self):
        pass

#search book information;return the set of the filtered books
class SearchBook(Search):
    def __init__(self, arg):
        try:
            self.arg = arg.decode("gbk")
        except:
            self.arg = arg
        self.arg = self.arg.replace(" ", "")
        self.target = []
        self.search()
        
    def search(self):
        if self.arg == "":
            return
        self.__searchAuthor()
        self.__searchCategor()
        self.__searchIsbn()
        self.__searchName()
        self.__searchPublisher()
        
    def __searchIsbn(self):
        result = Book.objects.filter(book_isbn__contains = self.arg)
        self.target.extend(result)
    
    def __searchName(self):
        result = Book.objects.filter(book_name__contains = self.arg)
        self.target.extend(result)
        
    def __searchCategor(self):
        result = Book.objects.filter(book_categorical__contains = self.arg)
        self.target.extend(result)
    
    def __searchAuthor(self):
        result = Book.objects.filter(book_auth_name__contains = self.arg)
        self.target.extend(result)
        
    def __searchPublisher(self):
        result = Book.objects.filter(book_publisher__contains = self.arg)
        self.target.extend(result)
        
    def getValue(self):
        return set(self.target)

#search web record; return the filtered record which in web;      
class SearchWebRecord(Search):
    def __init__(self, time1, time2, salesman):
        self.result = RecordWeb.objects.all()
        self.time1 = time1
        self.time2 = time2
        self.salesman = salesman
        self.search()
        
    def search(self):
        self.__searchTime()
        self.__searchSalesman()
        
    def __searchTime(self):
        if self.time1 == "all" or self.time1 == "" or self.time2 == "":
            pass
        else:
            date1 = datetime.datetime.strptime(self.time1, "%Y-%m-%d") 
            date2 = datetime.datetime.strptime(self.time2, "%Y-%m-%d") 
            self.result = self.result.filter(web_time__range=(date1, date2))
        
    def __searchSalesman(self):
        if self.salesman == "all":
            pass
        else:            
            self.result = self.result.filter(web_sell_id=int(self.salesman))
            
    def getValue(self):
        return set(self.result)

#search book information by hot point        
class SearchBookByHot(Search):
    
    def __init__(self, num, state):
        self.num = int(num)
        self.state = state
        self.result = []
        self.search()
    
    def search(self):
        if self.state == "increment":
            self.result = Book.objects.order_by('book_hot_point')[:self.num + 1]            
        else:
            self.result = Book.objects.order_by('-book_hot_point')[:self.num + 1]  
            
    def getValue(self):
        return set(self.result)
            
