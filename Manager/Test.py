#-*- coding:utf-8 -*-
from Search import SearchBook
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def sin(request):
    string = request.REQUEST.get("q")
    obj = SearchBook(string)
    ss = obj.getValue()
    return render(request, "search.html", {"value": ss})
