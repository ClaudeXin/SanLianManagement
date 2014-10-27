from django.http import HttpResponse
from Manager.models import Customer

def customLogin(request):
    userid = request.REQUEST.get("account", "none")
    password = request.REQUEST.get("password", "none")
    try:
        object = Customer.objects.get(cust_account=userid)
        if object.cust_password == password:
            return HttpResponse(object.cust_id)
        else:
            return HttpResponse("false")
    except:
        return HttpResponse("false")
