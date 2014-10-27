# -*- coding:utf-8 -*-
from django.db import models


class Book(models.Model):
    book_isbn = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=1)
    book_auth_name = models.CharField(max_length=1)
    book_publisher = models.CharField(max_length=1)
    book_publish_time = models.DateField()
    book_img_url = models.CharField(max_length=1)
    book_word = models.IntegerField()
    book_categorical = models.CharField(max_length=20)
    book_introduce = models.CharField(max_length=1)
    book_price = models.FloatField()
    book_save_num = models.IntegerField()
    book_hot_point = models.IntegerField()
    book_discount = models.FloatField()
    book_remain = models.IntegerField()
    book_sold_num = models.IntegerField()
    
    def __str__(self):
        return self.book_name.encode("utf-8")
        
    def insert(self, args):
        self.book_isbn = args["book_isbn"]
        self.book_name = args["book_name"]
        self.book_auth_name = args["book_auth_name"]
        self.book_publisher = args["book_publisher"]
        self.book_publish_time = args["book_publish_time"]
        self.book_img_url = args["book_img_url"]
        self.book_word = args["book_word"]
        self.book_categorical = args["book_categorical"]
        self.book_introduce = args["book_introduce"]
        self.book_price = args["book_price"]
        self.book_save_num = 0
        self.hot_point = 0
        self.discount = 1
        self.remain = 0
        self.sold_num = 0

        
class Operator(models.Model):
    oper_id = models.IntegerField(primary_key=True)
    oper_type = models.CharField(max_length=10)
    oper_detail = models.CharField(max_length=1)
    
    def __str__(self):
        return self.oper_type.encode("utf-8")
        
        
class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_account = models.CharField(max_length=40)
    cust_name = models.CharField(max_length=10)
    cust_password = models.CharField(max_length=20)
    cust_wechat = models.CharField(max_length=11)
    cust_phone = models.CharField(max_length=11)
    cust_head = models.CharField(max_length=1)
    cust_honest = models.IntegerField()
    cust_address = models.IntegerField()
    
    def __str__(self):
        return self.cust_name.encode("utf-8")

        
class Seller(models.Model):
    sell_id = models.IntegerField(primary_key=True)
    sell_password = models.CharField(max_length=20)
    sell_wechat = models.CharField(max_length=11)
    sell_name = models.CharField(max_length=20)
    sell_phone = models.CharField(max_length=11)
    sell_shop = models.IntegerField() #use shop table
    sell_account = models.CharField(max_length=40)
    
    def __str__(self):
        return self.sell_name.encode("utf-8")

        
class Address(models.Model):
    addr_id = models.IntegerField(primary_key=True)
    addr_cont = models.CharField(max_length=20)
    addr_prov = models.CharField(max_length=20)
    addr_city = models.CharField(max_length=20)
    addr_region = models.CharField(max_length=20)
    addr_street = models.CharField(max_length=20)
    addr_detail = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.addr_id)

class Man(models.Model):
    man_id = models.IntegerField(primary_key=True)
    man_account = models.CharField(max_length=40)
    man_password = models.CharField(max_length=20)
    man_name = models.CharField(max_length=10)
    man_wechat = models.CharField(max_length=11)
    man_phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.man_name.encode("utf-8")
        
        
class Bookshop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=20)
    shop_address = models.IntegerField() #use address table
    shop_manager = models.IntegerField() #use boss table
    
    def __str__(self):
        return self.shop_name.encode("utf-8")
        

class Comment(models.Model):
    com_id = models.IntegerField(primary_key=True)
    com_cust_id = models.IntegerField()
    com_book_id = models.IntegerField()
    com_star = models.IntegerField()
    com_text = models.CharField(max_length=1)
    com_time = models.DateTimeField()
    
    def __str__(self):
        return str(self.com_id)

class Collect(models.Model):
    coll_id = models.IntegerField(primary_key=True)
    coll_cust_id = models.IntegerField()
    coll_book_id = models.IntegerField()
    coll_time = models.DateTimeField()
    coll_type = models.CharField(max_length=1)
    
    def __str__(self):
        return str(self.coll_id)

class Log(models.Model):
    log_id = models.IntegerField(primary_key=True)
    log_userid = models.IntegerField()
    log_operator_id = models.IntegerField()
    log_permiss = models.IntegerField()
    log_time = models.DateTimeField()
    
    def __str__(self):
        return str(self.log_time)
    
class OrderBook(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_cust_id = models.IntegerField()
    order_book_id = models.IntegerField()
    order_sell_id = models.IntegerField()
    order_time = models.DateTimeField()
    order_han_time = models.DateTimeField()
    order_type = models.IntegerField()
    
    def __str__(self):
        return str(self.order_cust_id)

class RecordLocal(models.Model):
    local_id = models.IntegerField(primary_key=True)
    local_sell_id = models.IntegerField()
    local_book_id = models.IntegerField()
    local_time = models.DateTimeField()
    local_discount = models.FloatField()
    
    def __str__(self):
        return str(self.local_id)

class RecordWeb(models.Model):
    web_id = models.IntegerField(primary_key=True)
    web_cust_id = models.IntegerField()
    web_book_id = models.IntegerField()
    web_sell_id = models.IntegerField()
    web_time = models.DateTimeField()
    web_discount = models.FloatField()
    
    def __str__(self):
        return str(self.web_id)
    
class StoreBook(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_book_id = models.IntegerField()
    store_shop = models.IntegerField()
    store_time = models.DateTimeField()
    store_save = models.IntegerField()
    
    def __str__(self):
        return str(self.store_id)

class BlackList(models.Model):
    black_id = models.IntegerField(primary_key=True)
    black_account = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.black_id)
