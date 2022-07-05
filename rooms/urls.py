from django.urls import path
from django.conf.urls import url 
from . import views

app_name = 'rooms'
#register this in main urls folder
urlpatterns = [
    url(r'^$', views.block_list, name="room_list"),
    url(r'^(?P<block>[\w-]+)/(?P<floor>[\w-]+)/$', views.block_rooms, name="block_rooms")
]