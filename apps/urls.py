from django.conf.urls import url
from django.urls import path
from apps import views

urlpatterns = [
    url('^$', views.runner_check, name='check'),
    path('testcase/new/', views.post_new, name='testcase_new'),
]
