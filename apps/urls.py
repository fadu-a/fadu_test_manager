from django.conf.urls import url
from django.urls import path
from apps import views

urlpatterns = [
    url('^$', views.runner_check, name='check'),
    path('new/', views.post_new, name='new'),
]
