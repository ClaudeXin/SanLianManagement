from django.conf.urls import url, patterns
import display
import handle


urlpatterns = patterns('',
    url(r'^$', display.login, name='login'),
    url(r'^login/$', display.login, name='login'),
    url(r'^index/$', display.index, name='index'),
    url(r'^showteam/$', display.showTeam, name='showteam'),       
    url(r'^managerment/$', display.showInforManager, name='showinformanager'),
    url(r'^showconf/$', display.showConfMining, name='showconfmining'),
    url(r'^mining/$', handle.runMining, name='webming'),
    url(r'^search/$', handle.search, name='search'),
    url(r'^seller/change/$', handle.changeSeller, name="change"),
    url(r'^seller/add/$', display.showAddPage, name="add"),
    url(r'^seller/handleadd/$', handle.handleAdd, name="handleadd"),
   
)
