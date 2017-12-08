from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.post_list, name='post_list'),
url(r'^ciccc/',views.joke, name='ciccc'),#name means name for 'ciccc/'
]