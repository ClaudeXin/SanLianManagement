#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Man
from models import Seller
from obtain import webming
from managerbean import showBookDetail
from display import showInforManager

        
def runMining(request):
     	try:
        		manager_id = request.session["manager_id"]
        		man = Man.objects.get(man_id=manager_id)
	except:
        		return render(request, 'manager/login.html')

    	index = int(request.REQUEST.get("indexnum"))
    	thread = int(request.REQUEST.get("threadnum"))
    	return webming(request, index, thread, "manager/loadok.html")    

def search(request):
     	try:
        		manager_id = request.session["manager_id"]
        		man = Man.objects.get(man_id=manager_id)
	except:
        		return render(request, 'manager/login.html')	        		
	arg = request.REQUEST.get("searchargs") 
	page = request.REQUEST.get("page", "1")
	bookset = showBookDetail(arg).getValue()
	page = int(page)
	if page == 0:
		page = 1
	begin = (page - 1) * 5
	tmpend = (begin + 1) * 5
	if tmpend >= len(bookset):
		end = len(bookset) - 1
	else:
		end = tmpend		
	book = bookset[begin: end]
	return render(request, "manager/mutiinfor.html", {"books": book, "page":page, "arg": arg, "begin": page - 1, "end": page + 1})

def changeSeller(request):
	try:
        		manager_id = request.session["manager_id"]
        		man = Man.objects.get(man_id=manager_id)
	except:
        		return render(request, 'manager/login.html')
	del_option = request.POST.get("delete", "none")
	cha_option = request.POST.get("change", "none")
	sellerid = request.POST.get("sellid")

	seller = Seller.objects.get(sell_id=sellerid)

	if del_option == 'none' and cha_option != 'cha_option':

		phone = request.POST.get("phone", "none")
		wechat = request.POST.get("wechat", "none")
		if len(phone) != 11:
			return render(request, "manager/loadok.html", {"message": "错误的手机号"})
		seller.sell_phone = phone
		seller.sell_wechat = wechat
		seller.save()
		return showInforManager(request)
	elif del_option != 'none' and cha_option == 'none':
		seller.delete()
		return showInforManager(request)
	else:
		return render(request, "manager/loadok.html", {"message": "未知错误"})

def handleAdd(request):
	try:
        		manager_id = request.session["manager_id"]
        		man = Man.objects.get(man_id=manager_id)
	except:
        		return render(request, 'manager/login.html')

	sellid = request.POST.get("sellid")
	sellname = request.POST.get("sellname")
	sellaccount = request.POST.get("sellaccount")
	sellpassword = request.POST.get("sellpassword")
	sellphone = request.POST.get("sellphone")
	sellwechat = request.POST.get("sellwechat")

	if len(sellid) != 4:
		return render(request, "manager/addseller.html", {"message": "编号必须为四位"})
	try:
		int(sellid)
	except:
		return render(request, "manager/addseller.html", {"message": "编号必须为四位数字"})
	seller = Seller()
	seller.sell_id = sellid
	seller.sell_phone = sellphone
	seller.sell_name = sellname
	seller.sell_account = sellaccount
	seller.sell_wechat = sellwechat
	seller.sell_password = sellpassword
	seller.sell_shop = manager_id
	seller.save()      	
	return showInforManager(request)

