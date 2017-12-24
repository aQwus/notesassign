from django.conf.urls import url
from notesite.views import loggedin,auth_view,register
from .views import index_view,add_note

app_name='notes'

urlpatterns = [
    url(r'^loggedin/$',loggedin,name='loggedin'),
    url(r'^auth/$',auth_view,name='authenticate'),
    url(r'^addnote/', add_note, name='addnote'),
    url(r'^$', index_view, name='index'),
]
