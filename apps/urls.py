from django.conf.urls import url
from apps import views

urlpatterns = [
    url('^$', views.testRunner_check, name='check'),
]
