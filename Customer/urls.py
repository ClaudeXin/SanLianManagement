from django.conf.urls import url, patterns
import Response


urlpatterns = patterns('',
    url(r'^login$', Response.customLogin, name='cust_login'),
    
)