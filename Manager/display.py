#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from obtain import webming 
from models import Man, RecordWeb, Seller
from models import Book
from managerbean import ShowIndexWebRecord, ShowBookCase


def showTeam(request):
    try:
        manager_id = request.session["manager_id"]
        man = Man.objects.get(man_id=manager_id)
    except:
        return render(request, 'manager/login.html')       
    return render(request, 'manager/showteam.html')

def index(request):
    try:
        manager_id = request.session["manager_id"]
        man = Man.objects.get(man_id=manager_id)
    except:
        return render(request, 'manager/login.html')
    #init option
    try:
        salesoption = Seller.objects.all()
    except:
        pass        
    #get the input thing
    time1 = request.REQUEST.get("salesdate1", "all")
    time2 = request.REQUEST.get("salesdate2", "all")
    salesman = request.REQUEST.get("salesid", "all")
    booknum = request.REQUEST.get("booknum", "20")
    state = request.REQUEST.get("state", "decrement")
    
    record = ShowIndexWebRecord(time1, time2, salesman).getValue()
    book = ShowBookCase(booknum, state).getValue()   
    
    return render(request, 'manager/index.html', {"record":record, "book":book, 
        "salesoption":salesoption})
 
 
def login(request):
    username = request.POST.get("username", "None")
    password = request.POST.get("password", "None")    
    message = None
    if username == "None" and password == "None":
        return render(request, "manager/login.html", {"message": message})
    else:
        try:
            obj = Man.objects.get(man_account = username)
        except:
            message = "账户名错误"
            return render(request, "manager/login.html", {"message": message})
        if obj.man_password == password:
            request.session["manager_id"] = int(obj.man_id)
            return index(request)
        else:            
            message = "密码错误"
            return render(request, "manager/login.html", {"message": message})


def showConfMining(request):
    try:
        manager_id = request.session["manager_id"]
        man = Man.objects.get(man_id=manager_id)
    except:
        return render(request, 'manager/login.html')
        
    return render(request, 'manager/dict.html')

def showInforManager(request):
    try:
        manager_id = request.session["manager_id"]
        man = Man.objects.get(man_id=manager_id)
    except:
        return render(request, 'manager/login.html')
    book_num = 0;
    book_cata = Book.objects.distinct().values("book_categorical")
    book = Book.objects
    cata = []
    for value in book_cata:
        temp = {}
        size = len(book.filter(book_categorical = value["book_categorical"]))
        temp["name"] = value["book_categorical"]
        temp["value"] = size
        book_num += size
        cata.append(temp)

    seller = Seller.objects.all()        
    return render(request, 'manager/informanager.html', {"booknum": book_num, "bookcate": cata, "seller":seller})

def showAddPage(request):
    try:
        manager_id = request.session["manager_id"]
        man = Man.objects.get(man_id=manager_id)
    except:
        return render(request, 'manager/login.html')

    return render(request, 'manager/addseller.html')
