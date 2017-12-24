from django.conf.urls import url
from notesite.views import loggedin,auth_view

app_name='notes'

urlpatterns = [
    url(r'^loggedin/$',loggedin,name='loggedin'),
    url(r'^auth/$',auth_view,name='authenticate'),
]
