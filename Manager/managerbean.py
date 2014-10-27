#-*-coding:utf-8-*-
from models import Book, Seller, Customer
from search import SearchWebRecord, SearchBookByHot
from search import SearchBook
import re

class filterResult():
    def filterWork(self):
        pass
    def getValue(self):
        pass

class ShowIndexWebRecord(filterResult):
    def __init__(self, time1, time2, salesman):     
        self.target = SearchWebRecord(time1, time2, salesman).getValue()   
        self.result = []
        self.filterWork()
    
    def filterWork(self):
        for element in self.target:
            temp = {}
            #translate the objects
            customer = Customer.objects.get(cust_id=element.web_cust_id)
            seller = Seller.objects.get(sell_id=element.web_sell_id)
            book = Book.objects.get(book_isbn=element.web_book_id)
            name_match = re.compile(u"\uFF08.*?\uFF09")
            #create the keys-values relationship
            temp["web_cust"] = customer.cust_name
            temp["web_sell_id"] = seller.sell_name
            temp["web_sell_price"] = str(element.web_discount * book.book_price)
            temp["web_time"] = element.web_time.strftime('%Y年%m月%d日%H时%M分%S秒')
            temp["web_book_id"] = element.web_book_id #re.sub(name_match, "", book.book_name).replace("&nbsp;", "")
            self.result.append(temp)
        
    def getValue(self):
        return self.result
        
class ShowBookCase(filterResult):
    def __init__(self, num, state):
        self.target = SearchBookByHot(num, state).getValue()
        self.result = []
        self.filterWork()
        
    def filterWork(self):        
        for element in self.target:
            temp = {}
            name_match = re.compile(u"\uFF08.*?\uFF09")
            temp["book_name"] = re.sub(name_match, "", element.book_name).replace("&nbsp;", "")
            temp["book_isbn"] = element.book_isbn
            if element.book_remain == None:
                element.book_remain = 0                
            temp["book_remain"] = element.book_remain
            if element.book_remain == None:
                element.book_remain = 0                
            temp["book_hot_point"] = element.book_hot_point
            element.save()
            self.result.append(temp)
        pass
    def getValue(self):
        return self.result

class showBookDetail(filterResult):
    def __init__(self, arg):
        self.target = SearchBook(arg).getValue()
        self.result = []
        self.filterWork()

    def filterWork(self):
        for element in self.target:
            temp = {}
            temp["book_isbn"] = element.book_isbn
            temp["book_name"] = element.book_name
            temp["book_auth_name"] = element.book_auth_name

            publisher = element.book_publisher
            if not publisher:
                temp["book_publisher"] = "未知"
            else:
                temp["book_publisher"] = publisher

            publish_time = element.book_publish_time
            if not publish_time:
                temp["book_publish_time"] = ""
            else:
                temp["book_publish_time"] = publish_time

            introduce = element.book_introduce
            if not introduce:
                temp["book_introduce"] = ""
            else:
                temp["book_introduce"] = introduce

            word = element.book_word
            if not word:                 
                temp["book_word"] = ""
            else:
                temp["book_word"] = word
            self.result.append(temp)        

    def getValue(self):
        return self.result        