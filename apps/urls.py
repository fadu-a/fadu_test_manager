from django.conf.urls import include, url
from apps import views
from django.urls import path

urlpatterns = [
        url('^$', views.testRunner_check, name='check'),

]

